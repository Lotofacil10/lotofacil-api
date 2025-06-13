# backend/app/api/routes_ia.py

import asyncio
import random
from collections import Counter

import httpx
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["IA"])

API_BASE = "https://loteriascaixa-api.herokuapp.com/api/lotofacil"

@router.get(
    "/gerar",
    summary="Gera X jogos de Lotofácil baseados nos 25 últimos concursos"
)
async def gerar_com_ia(
    qtd_jogos: int = 1,
    dezenas_por_jogo: int = 15
):
    # 1) Busca o último concurso via /latest
    async with httpx.AsyncClient() as client:
        ultimo_resp = await client.get(f"{API_BASE}/latest")
    if ultimo_resp.status_code != 200:
        raise HTTPException(status_code=500, detail="Não foi possível obter o último concurso")
    ultimo_data = ultimo_resp.json()

    # 2) A chave correta é "concurso"
    ultimo_numero = ultimo_data.get("concurso")
    if not ultimo_numero:
        raise HTTPException(status_code=500, detail="Número do último concurso não encontrado")

    # 3) Pega os 25 últimos concursos EM PARALELO
    concursos = [ultimo_numero - i for i in range(25)]
    async with httpx.AsyncClient() as client:
        tasks = [client.get(f"{API_BASE}/{num}") for num in concursos]
        responses = await asyncio.gather(*tasks, return_exceptions=True)

    todas_dezenas = []
    for resp in responses:
        if isinstance(resp, Exception):
            continue
        if resp.status_code == 200:
            data = resp.json()
            # tente ambos os campos "dezenas" ou "dezenasOrdemSorteio"
            dezenas = data.get("dezenas") or data.get("dezenasOrdemSorteio") or []
            todas_dezenas.extend(int(d) for d in dezenas)

    if not todas_dezenas:
        raise HTTPException(status_code=500, detail="Nenhuma dezena coletada")

    # 4) Conta frequência e ordena
    freq = Counter(todas_dezenas)
    mais_frequentes = [dez for dez, _ in freq.most_common()]

    # 5) Gera os jogos
    jogos = []
    for _ in range(qtd_jogos):
        # escolhe entre os top-20 mais frequentes
        selecionadas = random.sample(mais_frequentes[:20], dezenas_por_jogo)
        jogos.append(sorted(selecionadas))

    # 6) Retorna o JSON final
    return {
        "concursos_analisados": 25,
        "frequencia": dict(freq),
        "jogos_gerados": jogos
    }

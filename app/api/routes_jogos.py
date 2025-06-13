from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from app.schemas.jogo_schema import JogoSchema
from app.services import jogo_service
from app.core.database import db


router = APIRouter(
    prefix="/jogos",
    tags=["Jogos"]
)


# 🔸 Listar Jogos
@router.get("/", response_model=List[dict])
async def listar_jogos():
    return await jogo_service.listar_jogos(db)


# 🔸 Buscar Jogo por ID
@router.get("/{jogo_id}", response_model=dict)
async def buscar_jogo(jogo_id: str):
    jogo = await jogo_service.buscar_jogo(db, jogo_id)
    if not jogo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Jogo não encontrado")
    return jogo


# 🔸 Criar Jogo
@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def criar_jogo(jogo: JogoSchema):
    return await jogo_service.criar_jogo(db, jogo)


# 🔸 Atualizar Jogo
@router.put("/{jogo_id}", response_model=dict)
async def atualizar_jogo(jogo_id: str, dados: dict):
    atualizado = await jogo_service.atualizar_jogo(db, jogo_id, dados)
    if not atualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Jogo não encontrado")
    return {"mensagem": "Jogo atualizado com sucesso"}


# 🔸 Deletar Jogo
@router.delete("/{jogo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_jogo(jogo_id: str):
    deletado = await jogo_service.deletar_jogo(db, jogo_id)
    if not deletado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Jogo não encontrado")
    return {"mensagem": "Jogo deletado com sucesso"}
from collections import Counter
import requests
from random import sample

# 🔸 Gerar Jogos com IA (frequência das dezenas dos últimos concursos)
@router.post("/gerar-com-ia", response_model=List[List[str]])
async def gerar_jogos_com_ia(qtd_jogos: int = 10):
    concursos = []
    
    # Buscar os últimos 20 concursos
    for n in range(20):
        try:
            resp = requests.get(f"https://loteriascaixa-api.herokuapp.com/api/lotofacil/{3407 - n}")
            if resp.status_code == 200:
                dezenas = resp.json().get("dezenas")
                if dezenas:
                    concursos.append(dezenas)
        except:
            continue

    # Contar frequência de dezenas
    todas = [dez for jogo in concursos for dez in jogo]
    mais_frequentes = [dez for dez, _ in Counter(todas).most_common(20)]

    # Gerar jogos com base nas mais frequentes
    jogos = []
    for _ in range(qtd_jogos):
        jogo = sorted(sample(mais_frequentes, 15))
        jogos.append(jogo)

    return jogos

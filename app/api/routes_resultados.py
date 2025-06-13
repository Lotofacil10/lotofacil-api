# backend/app/api/routes_resultados.py

from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter(tags=["Resultados"])

API_BASE = "https://loteriascaixa-api.herokuapp.com/api/lotofacil"

@router.get("/oficial/ao-vivo", summary="Resultado Oficial Ao Vivo")
async def get_resultado_oficial():
    async with httpx.AsyncClient() as client:
        # Usa /latest em vez de /concurso/ao-vivo
        resp = await client.get(f"{API_BASE}/latest")
        if resp.status_code == 200:
            return resp.json()
    raise HTTPException(status_code=500, detail="Erro ao buscar resultado oficial")

@router.get("/ao-vivo/{numero}", summary="Resultado Por Concurso")
async def get_resultado_por_concurso(numero: int):
    async with httpx.AsyncClient() as client:
        # A URL /lotofacil/{numero} já retorna o JSON do concurso
        resp = await client.get(f"{API_BASE}/{numero}")
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code == 404:
            raise HTTPException(status_code=404, detail="Concurso não encontrado")
    raise HTTPException(status_code=500, detail="Erro ao buscar concurso")

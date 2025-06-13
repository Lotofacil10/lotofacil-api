from fastapi import APIRouter, HTTPException
from app.services.scraping_service import (
    scrapear_resultado_lotofacil,
    scrapear_resultado_por_numero
)

router = APIRouter(prefix="/resultados", tags=["Resultados"])

# 🔹 GET - Último resultado oficial ao vivo
@router.get("/oficial/ao-vivo")
async def resultado_oficial_ao_vivo():
    try:
        resultado = scrapear_resultado_lotofacil()

        if not resultado:
            raise HTTPException(status_code=422, detail="Resultado incompleto.")

        return resultado

    except Exception as e:
        print(f"❌ Erro ao buscar resultado oficial ao vivo: {e}")
        raise HTTPException(status_code=500, detail="Erro ao buscar resultado oficial ao vivo.")

# 🔹 GET - Concurso específico (ao vivo)
@router.get("/ao-vivo/{concurso}")
async def resultado_por_concurso(concurso: int):
    try:
        resultado = scrapear_resultado_por_numero(concurso)

        if not resultado:
            raise HTTPException(status_code=404, detail="Concurso não encontrado.")

        return resultado

    except Exception as e:
        print(f"❌ Erro ao buscar concurso {concurso}: {e}")
        raise HTTPException(status_code=500, detail="Erro ao buscar concurso.")

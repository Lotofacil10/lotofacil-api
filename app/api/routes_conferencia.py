from fastapi import APIRouter
from app.schemas.conferencia_schema import ConferenciaRequest, ConferenciaResponse
from app.services import conferencia_service


router = APIRouter(
    prefix="/conferencia",
    tags=["Conferência"]
)


@router.post("/", response_model=ConferenciaResponse)
async def conferir_jogo(payload: ConferenciaRequest):
    """
    🏆 Conferir um jogo com base no resultado fornecido.

    🔢 Envie um JSON com:
    - `jogo`: seu jogo (15 dezenas)
    - `resultado`: dezenas sorteadas no concurso

    🔍 Retorna quantos acertos e quais dezenas foram acertadas.
    """
    return conferencia_service.conferir_jogo(payload.jogo, payload.resultado)

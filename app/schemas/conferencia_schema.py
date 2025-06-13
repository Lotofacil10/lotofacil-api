from typing import List
from pydantic import BaseModel, Field


class ConferenciaRequest(BaseModel):
    jogo: List[int] = Field(..., min_items=15, max_items=15, description="Dezenas do jogo (15 dezenas)")
    resultado: List[int] = Field(..., min_items=15, max_items=15, description="Dezenas sorteadas no resultado (15 dezenas)")

    class Config:
        json_schema_extra = {  # ← Atualizado para Pydantic v2
            "example": {
                "jogo": [1, 3, 5, 7, 9, 11, 13, 14, 16, 18, 19, 21, 23, 24, 25],
                "resultado": [2, 3, 5, 7, 10, 11, 12, 14, 15, 18, 19, 21, 22, 24, 25]
            }
        }


class ConferenciaResponse(BaseModel):
    dezenas_jogo: List[int]
    dezenas_sorteadas: List[int]
    acertos: List[int]
    quantidade_acertos: int
    status: str

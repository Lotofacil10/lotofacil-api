from typing import List, Optional
from pydantic import BaseModel


class ResultadoSchema(BaseModel):
    concurso: int
    dezenas_sorteadas: List[int]
    data_concurso: Optional[str]

    class Config:
        json_schema_extra = {  # ← atualizado
            "example": {
                "concurso": 2850,
                "dezenas_sorteadas": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                "data_concurso": "2024-05-27"
            }
        }


class ResultadoResponseSchema(ResultadoSchema):
    id: str

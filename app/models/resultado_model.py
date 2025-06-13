from typing import Optional, List
from pydantic import BaseModel, Field
from bson import ObjectId
from app.utils.pyobjectid import PyObjectId
from datetime import date

class ResultadoModel(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    concurso: int = Field(...)
    dezenas: List[int] = Field(..., min_items=15, max_items=15)
    data_sorteio: Optional[date] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "concurso": 3020,
                "dezenas": [1, 3, 5, 7, 9, 10, 12, 14, 16, 18, 19, 21, 23, 24, 25],
                "data_sorteio": "2024-05-27"
            }
        }

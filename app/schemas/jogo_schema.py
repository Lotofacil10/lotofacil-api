from typing import List, Optional
from pydantic import BaseModel


class JogoSchema(BaseModel):
    nome: str
    dezenas: List[int]

    class Config:
        json_schema_extra = {  # ← atualizado
            "example": {
                "nome": "Jogo da Sorte",
                "dezenas": [1, 3, 5, 7, 9, 10, 11, 13, 14, 16, 18, 20, 22, 24, 25]
            }
        }


class JogoResponseSchema(JogoSchema):
    id: str
    criado_em: Optional[str]


from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId
from app.utils.pyobjectid import PyObjectId


class JogoBase(BaseModel):
    dezenas: List[int] = Field(..., min_items=15, max_items=15)
    criado_em: Optional[str] = None


class JogoCreate(JogoBase):
    pass


class JogoResponse(JogoBase):
    id: Optional[PyObjectId] = Field(alias="_id")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {  # ← atualizado
            "example": {
                "dezenas": [1, 3, 5, 7, 9, 10, 11, 13, 14, 16, 18, 20, 22, 24, 25],
                "criado_em": "2024-05-27 14:00"
            }
        }

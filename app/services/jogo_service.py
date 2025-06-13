from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.models.jogo_model import JogoModel
from app.schemas.jogo_schema import JogoSchema


# Coleção de Jogos
def get_collection(db: AsyncIOMotorDatabase):
    return db["jogos"]


# ➕ Criar Jogo
async def criar_jogo(db: AsyncIOMotorDatabase, jogo: JogoSchema) -> dict:
    jogo_dict = jogo.dict()
    jogo_dict["criado_em"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    result = await get_collection(db).insert_one(jogo_dict)
    jogo_dict["_id"] = str(result.inserted_id)
    return jogo_dict


# 🔍 Listar todos os Jogos
async def listar_jogos(db: AsyncIOMotorDatabase) -> List[dict]:
    jogos = []
    async for jogo in get_collection(db).find():
        jogo["_id"] = str(jogo["_id"])
        jogos.append(jogo)
    return jogos


# 🔍 Buscar Jogo por ID
async def buscar_jogo(db: AsyncIOMotorDatabase, jogo_id: str) -> Optional[dict]:
    jogo = await get_collection(db).find_one({"_id": ObjectId(jogo_id)})
    if jogo:
        jogo["_id"] = str(jogo["_id"])
    return jogo


# ✏️ Atualizar Jogo
async def atualizar_jogo(db: AsyncIOMotorDatabase, jogo_id: str, dados: dict) -> bool:
    result = await get_collection(db).update_one(
        {"_id": ObjectId(jogo_id)}, {"$set": dados}
    )
    return result.modified_count == 1


# ❌ Deletar Jogo
async def deletar_jogo(db: AsyncIOMotorDatabase, jogo_id: str) -> bool:
    result = await get_collection(db).delete_one({"_id": ObjectId(jogo_id)})
    return result.deleted_count == 1

from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]


async def test_connection():
    try:
        # Verificar se consegue listar os bancos (é como um ping)
        databases = await client.list_database_names()
        print("🟢 Conexão bem-sucedida com MongoDB!")
        print("Bancos disponíveis:", databases)
    except Exception as e:
        print("🔴 Erro na conexão com MongoDB:", e)


if __name__ == "__main__":
    asyncio.run(test_connection())

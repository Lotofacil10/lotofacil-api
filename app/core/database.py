from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Carregar as variáveis do arquivo .env
load_dotenv()

# Pegar as variáveis de ambiente
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# Conectar ao MongoDB
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

print(f"🟢 Conectado ao MongoDB no banco: {DB_NAME}")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# importe os dois routers
from app.api.routes_resultados import router as resultados_router
from app.api.routes_ia import router as ia_router

load_dotenv()

app = FastAPI(
    title="API Lotofácil",
    version="1.0.0",
    description="Backend da Lotofácil com scraping ao vivo (sem banco de dados)."
)

# CORS para o front em http://localhost:5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"
    "https://web-production-72054.up.railway.app/api",],
    
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ⚙️ rotas de resultados vão estar em /api/resultados
app.include_router(
    resultados_router,
    prefix="/api/resultados",
    tags=["Resultados"]
)

# ⚙️ rotas de IA vão estar em /api/ia
app.include_router(
    ia_router,
    prefix="/api/ia",
    tags=["IA"]
)

@app.get("/")
async def root():
    return {"status": "API Lotofácil rodando perfeitamente ✅"}

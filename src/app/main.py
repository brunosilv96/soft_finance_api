from fastapi import FastAPI
from src.app.routers import v1_router

app = FastAPI()

app = FastAPI(
    title="Soft Finance",
    description="Gerenciador de finanças fácil e confiável",
    version="1.0.0"
)

app.include_router(v1_router)

@app.get("/v1")
def health_check() -> dict:
    return {"status": "OK"}

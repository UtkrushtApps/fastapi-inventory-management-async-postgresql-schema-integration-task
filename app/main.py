from fastapi import FastAPI
from app.routes import api

app = FastAPI(title="Inventory Management API")
app.include_router(api.router)

@app.get("/health")
async def health():
    return {"status": "ok"}

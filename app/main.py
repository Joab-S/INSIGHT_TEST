from fastapi import FastAPI
import requests_cache
from app.api.endpoints.urls import api_router

app = FastAPI(
    title = "API de Municípios do Ceará",
    description = "API útil para fornecer informações sobre os municípios do Ceará para um mapa iterativo.",
    version = "1.0.0"
)

requests_cache.install_cache(cache_name='insight_cache', backend='sqlite', expire_after=180)
app.include_router(api_router)
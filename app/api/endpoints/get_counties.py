from fastapi import APIRouter
from app.api.models.basic_county import BasicCounty
from app.services.ibge_service import fetch_ceara_counties
from app.utils.helpers import county_response_format
from typing import List

counties_router = APIRouter()

@counties_router.get("/", response_model=List[BasicCounty], summary="Listar Municípios do Ceará", description="Retorna uma lista com informações básicas de todos os municípios do Ceará.")
def get_counties():
    counties = fetch_ceara_counties()
    return [
        BasicCounty (
            codeibge=m["id"],
            name=m["nome"]
        )

    for m in counties]
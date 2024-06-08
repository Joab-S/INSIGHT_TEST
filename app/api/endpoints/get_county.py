from fastapi import APIRouter, HTTPException
from app.api.models.detailed_county import DetailedCounty
from app.utils.helpers import county_response_format
import requests

county_router = APIRouter()

@county_router.get("/{codeibge}", response_model=DetailedCounty, summary="Detalhes do Município", description="Retorna informações detalhadas de um município específico do Ceará.")
def get_detailed_county(codeibge: int):
    try:
        details = county_response_format(codeibge)
        return DetailedCounty (
                codeibge = codeibge,
                name = details["name"],
                area = details["area"],
                population = details["population"] if "population" in details else None,
                population_density = details["population_density"] if "population_density" in details else None,
                pib = details["pib"] if "pib" in details else None,
                income_per_capita = details["income_per_capita"] if "income_per_capita" in details else None
            )
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=404, detail="Município não encontrado")
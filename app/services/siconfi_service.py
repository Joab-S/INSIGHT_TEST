import requests
from fastapi import HTTPException

def fetch_ceara_counties_population_siconfi():
        url = "https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes"

        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise HTTPException(status_code=500, detail=f"Erro ao buscar informações do município: {e}")
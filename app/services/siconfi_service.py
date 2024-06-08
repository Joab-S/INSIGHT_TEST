import requests
import json
from fastapi import HTTPException
from app.core.config import redis_client, expiration_time

def fetch_ceara_counties_population_by_codibge(county_codibge):
    cache_key = f"siconfi:entes:{county_codibge}"
    cached_data = redis_client.get(cache_key)
    #print("cached_data: ", cached_data)

    if cached_data:
        county_by_codibge = json.loads(cached_data)
        #print("Dados buscados no cachê")
    else:
        url = "https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes"

        county_by_codibge = None
        try:
            response = requests.get(url)
            response.raise_for_status()
            counties = response.json()
        except requests.RequestException as e:
            raise HTTPException(status_code=500, detail=f"Erro ao buscar informações do município: {e}")
        
        for county in counties["items"]:
            redis_client.setex(f"siconfi:entes:{county['cod_ibge']}", expiration_time, json.dumps(county))
            if county["cod_ibge"] == county_codibge:
                county_by_codibge = county

        #print("Dados buscados na URL")

    return county_by_codibge
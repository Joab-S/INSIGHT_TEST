import requests
import json
from fastapi import HTTPException
from app.services.siconfi_service import fetch_ceara_counties_population_siconfi
from app.core.config import redis_client, expiration_time

def fetch_ceara_counties_population_by_codibge(county_codibge):
    cache_key = f"siconfi:entes:{county_codibge}"
    cached_data = redis_client.get(cache_key)

    if cached_data:
        county_by_codibge = json.loads(cached_data)
        #print("Dados buscados no cachê")
    else:
        county_by_codibge = None

        counties = fetch_ceara_counties_population_siconfi()
        
        for county in counties["items"]:
            redis_client.setex(f"siconfi:entes:{county['cod_ibge']}", expiration_time, json.dumps(county))
            if county["cod_ibge"] == county_codibge:
                county_by_codibge = county

        #print("Dados buscados na URL")

    return county_by_codibge
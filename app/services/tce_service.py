import requests
from fastapi import HTTPException
import json
from datetime import date
from concurrent.futures import ThreadPoolExecutor
from app.core.config import redis_client, expiration_time

def fetch_details_county(codibge):
    url = f"https://api-dados-abertos.tce.ce.gov.br/municipios?geoibgeId={codibge}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        details = response.json()
        return details
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar dealhes sobre o município: {e}")


def fetch_programs_for_year_month(tcecode, date):
    url = f"https://api-dados-abertos.tce.ce.gov.br/programas?codigo_municipio={tcecode}&exercicio_orcamento={date}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["data"]
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar informações do município: {e}")

def fetch_government_programs(codibge, year=None):
    details_county_data = fetch_details_county(codibge)["data"][0]
    tcecode = details_county_data["codigo_municipio"]

    if year is None:
        year = int(str(date.today().year) + "00")
    elif int(year) < 2007:
        programs = []
        cache_key = f"tce:programs:{codibge}:{int(str(year) + '00')}"
        cached_data = redis_client.get(cache_key)

        if cached_data:
            programs = json.loads(cached_data)
        else:
            months = [str(i).zfill(2) for i in range(1, 13)]
            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(fetch_programs_for_year_month, tcecode, (str(year) + str(month))) for month in months]
                for future in futures:
                    programs += future.result()
            redis_client.setex(cache_key, expiration_time, json.dumps(programs))
    else:
        year = int(str(year) + "00")
        cache_key = f"tce:programs:{codibge}:{year}"
        cached_data = redis_client.get(cache_key)

        if cached_data:
            programs = json.loads(cached_data)
        else:
            programs = fetch_programs_for_year_month(tcecode, year)
            redis_client.setex(cache_key, expiration_time, json.dumps(programs))

    return programs
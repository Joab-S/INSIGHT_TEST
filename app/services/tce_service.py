import requests
import json
from fastapi import HTTPException
from app.core.config import redis_client, expiration_time

def fetch_details_county_tce(codibge):
    print("DETAILS COUNTY")
    cache_key = f"tce:details_county:{codibge}"
    cached_data = redis_client.get(cache_key)

    if cached_data:
        print("CACHE")
        return json.loads(cached_data)
    else:
        print("URL: Vai tentar entrar no tce:municipios")
        url = f"https://api-dados-abertos.tce.ce.gov.br/municipios?geoibgeId={codibge}"
        try:
            response = requests.get(url, verify=False)
            response.raise_for_status()
            details = response.json()
            redis_client.setex(cache_key, expiration_time, json.dumps(details))
            print("DETALHES: ", details)
            return details
        except requests.RequestException as e:
            raise HTTPException(status_code=500, detail=f"Erro ao buscar dealhes sobre o município: {e}")


def fetch_programs_tce(tcecode, date):
    url = f"https://api-dados-abertos.tce.ce.gov.br/programas?codigo_municipio={tcecode}&exercicio_orcamento={date}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["data"]
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar informações do programa: {e}")


def fetch_program_expenses_tce(tcecode, date):
    url = f"https://api-dados-abertos.tce.ce.gov.br/despesa_projeto_atividade?codigo_municipio={tcecode}&exercicio_orcamento={date}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["data"]
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar informações das desepesas do programa: {e}")
    

def fetch_organs_tce(tcecode, date, organcode):
    url = f"https://api-dados-abertos.tce.ce.gov.br/orgaos?codigo_municipio={tcecode}&exercicio_orcamento={date}"
    if (organcode):
        url += f"&codigo_orgao={organcode}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["data"]
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar informações das desepesas do programa: {e}")
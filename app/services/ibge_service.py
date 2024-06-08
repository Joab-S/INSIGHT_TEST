import requests
from fastapi import HTTPException

def fetch_ceara_counties():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/CE/municipios"
    try:
        response = requests.get(url)
        response.raise_for_status()
        counties = response.json()
        return counties
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar municípios do Ceará: {e}")


def feach_ceara_county(id):
    url= f"https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        county = response.json()
        return county
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar município com o ID {id}: {e}")


def county_mesh_metadata(id):
    url = f"https://servicodados.ibge.gov.br/api/v3/malhas/municipios/{id}/metadados"
    try:
        response = requests.get(url)
        response.raise_for_status()
        metadata = response.json()
        return metadata
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar metadados do município com o ID {id}: {e}")


def county_mesh(id):
    url = f"https://servicodados.ibge.gov.br/api/v3/malhas/municipios/{id}?formato=application/vnd.geo+json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        mesh = response.json()
        return mesh
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar malha do município com o ID {id}: {e}")

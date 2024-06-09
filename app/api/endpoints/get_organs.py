from fastapi import APIRouter, Query
from app.api.models.organ import Organ
from app.api.controllers.fetch_organs import fetch_organs
from typing import List

organs_router = APIRouter()

@organs_router.get("/{codeibge}/organs", response_model=List[Organ], summary="Listagem de Orgãos Municipais", description="Retorna uma lista com os Orgãos Municipais.")
def get_organs(codeibge, year: int = Query(None, description="Ano do Exercício do Orçamento. Informe o ano no formato AAAA. Dados a partir de 2003, até os anos atuais."), organcode: str = Query(None, description="Código do Órgão")):
    organs = fetch_organs(codeibge, year, organcode)
    return [
        Organ (
            organ_code = o["codigo_orgao"],
            organ_name = o["nome_orgao"],
            unit_type_code = o["codigo_tipo_unidade"],
            organ_cgc = o["cgc_orgao"]
        )
        for o in organs]
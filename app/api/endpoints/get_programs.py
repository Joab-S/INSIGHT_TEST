from fastapi import APIRouter, HTTPException, Query
from app.api.models.program import Program
from app.services.tce_service import fetch_government_programs
import requests
from typing import List

programs_router = APIRouter()

@programs_router.get("/{codeibge}/programs", response_model=List[Program], summary="Detalhes de Programas de Gorveno por Município", description="Relação de Programas de Governo estabelecidos na Lei de Orçamento Municipal.")
def get_government_programs(codeibge: int, year: int = Query(None, description="Ano do Exercício do Orçamento. Informe o ano no formato AAAA. Dados a partir de 2003, até os anos atuais.")):
    try:
        details = fetch_government_programs(codeibge, year)

        if details is None or details == []:
            return []
        return [
        Program (
            cod_program = program["codigo_programa"],
            name = program["nome_programa"]
        )
        
        for program in details]
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=404, detail="Erro ao buscar programas")
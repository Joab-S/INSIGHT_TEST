from fastapi import APIRouter, HTTPException, Query
from app.api.models.program_expense import ProgramExpense
from app.api.models.function import Function
from app.api.controllers.fetch_program_expenses_controller import fetch_program_expenses
import requests
from typing import List

programs_expenses_router = APIRouter()

@programs_expenses_router.get("/{codeibge}/programs/{codprogram}/program-expenses", response_model=List[ProgramExpense], summary="Detalhes de despesas de Programas por Município", description="Relação de despesas de orçamento de Programas de Governo estabelecidos na Lei de Orçamento Municipal.")
def get_program_expenses(codeibge: int, codprogram: str, year: int = Query(None, description="Ano do Exercício do Orçamento. Informe o ano no formato AAAA. Dados a partir de 2003, até os anos atuais.")):
    try:
        details = fetch_program_expenses(codeibge, codprogram, year)

        if details is None or details == []:
            return []
        return [
        ProgramExpense (
            program_code = d["codigo_programa"],
            county_code = d["codigo_municipio"],
            exercise_budget = d["exercicio_orcamento"],
            org_code = d["codigo_orgao"],
            unit_code = d["codigo_unidade"],
            function = Function (
                function_code = d["funcao"]["codigo_funcao"],
                function_name = d["funcao"]["nome_funcao"]
            ),
            subfunction_code = d["codigo_subfuncao"],
            project_of_activity = d["codigo_projeto_atividade"],
            activity_project_number = d["numero_projeto_atividade"],
            number_subproject_activity = d["numero_subprojeto_atividade"],
            code_type_budget = d["codigo_tipo_orcamento"],
            activity_project_name = d["nome_projeto_atividade"],
            description_project_activity = d["descricao_projeto_atividade"],
            total_value_fixed_project_activity = d["valor_total_fixado_projeto_atividade"]
        )
        
        for d in details]
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=404, detail="Erro ao buscar programas")
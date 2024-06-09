import json
from datetime import date
from concurrent.futures import ThreadPoolExecutor
from app.core.config import redis_client, expiration_time
from app.services.tce_service import fetch_details_county_tce, fetch_program_expenses_tce

def fetch_program_expenses(codibge, codprogram, year=None):
    details_county_data = fetch_details_county_tce(codibge)["data"][0]
    tcecode = details_county_data["codigo_municipio"]

    program_expenses = []
    if year is None:
        year = int(str(date.today().year) + "00")
    elif int(year) < 2007:
        cache_key = f"tce:program_expenses:{codibge}:{int(str(year) + '00')}"
        cached_data = redis_client.get(cache_key)

        if cached_data:
            program_expenses = json.loads(cached_data)
        else:
            months = [str(i).zfill(2) for i in range(1, 13)]
            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(fetch_program_expenses_tce, tcecode, (str(year) + str(month))) for month in months]
                for future in futures:
                    program_expenses += future.result()
            redis_client.setex(cache_key, expiration_time, json.dumps(program_expenses))
    else:
        year = int(str(year) + "00")
    
    cache_key = f"tce:program_expenses:{codibge}:{year}"
    cached_data = redis_client.get(cache_key)

    if cached_data:
        program_expenses = json.loads(cached_data)
    else:
        program_expenses = fetch_program_expenses_tce(tcecode, year)
        redis_client.setex(cache_key, expiration_time, json.dumps(program_expenses))

    filtered_expenses = [expense for expense in program_expenses if expense.get("codigo_programa") == str(codprogram)]

    for expense in filtered_expenses:
        codigo_pa = expense.get("codigo_projeto_atividade")
        if codigo_pa in ["1", "3", "5", "7"]:
            expense["codigo_projeto_atividade"] = "Projetos"
        elif codigo_pa in ["2", "4", "6", "8"]:
            expense["codigo_projeto_atividade"] = "Atividades"
        elif codigo_pa == "9":
            expense["codigo_projeto_atividade"] = "Reserva de Contingência"
        else:  # "0"
            expense["codigo_projeto_atividade"] = "Operações Especiais"

        codigo_to = expense.get("codigo_tipo_orcamento")
        if codigo_to == "F":
            expense["codigo_tipo_orcamento"] = "Orçamento Fiscal"
        else:  # elif codigo_to == "S":
            expense["codigo_tipo_orcamento"] = "Orçamento da Seguridade Social"



    return filtered_expenses
import json
from datetime import date
from concurrent.futures import ThreadPoolExecutor
from app.core.config import redis_client, expiration_time
from app.services.tce_service import fetch_details_county_tce, fetch_programs_tce

def fetch_government_programs(codibge, year=None):
    details_county_data = fetch_details_county_tce(codibge)["data"][0]
    tcecode = details_county_data["codigo_municipio"]

    programs = []
    if year is None:
        year = int(str(date.today().year) + "00")
        print(year)
    elif int(year) < 2007:
        cache_key = f"tce:programs:{codibge}:{int(str(year) + '00')}"
        cached_data = redis_client.get(cache_key)

        if cached_data:
            programs = json.loads(cached_data)
        else:
            months = [str(i).zfill(2) for i in range(1, 13)]
            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(fetch_programs_tce, tcecode, (str(year) + str(month))) for month in months]
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
        programs = fetch_programs_tce(tcecode, year)
        redis_client.setex(cache_key, expiration_time, json.dumps(programs))

    return programs
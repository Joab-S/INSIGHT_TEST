import json
from datetime import date
from concurrent.futures import ThreadPoolExecutor
from app.core.config import redis_client, expiration_time
from app.services.tce_service import fetch_details_county_tce, fetch_organs_tce


def fetch_organs(codibge, year=None, organcode=None):
    details_county_data = fetch_details_county_tce(codibge)["data"][0]
    tcecode = details_county_data["codigo_municipio"]

    organs = []

    if year is None:
        year = int(str(date.today().year) + "00")
    elif int(year) < 2007:
        cache_key = f"tce:organs:{codibge}:{int(str(year) + '00')}:{organcode or 'no_organcode'}"
        cached_data = redis_client.get(cache_key)

        if cached_data:
            print("cachê - <2007")
            organs = json.loads(cached_data)
        else:
            print("url - <2007")
            months = [str(i).zfill(2) for i in range(1, 13)]
            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(fetch_organs_tce, tcecode, (str(year) + str(month)), organcode) for month in months]
                for future in futures:
                    organs += future.result()
            redis_client.setex(cache_key, expiration_time, json.dumps(organs))
    else:
        year = int(str(year) + "00")

    cache_key = f"tce:organs:{codibge}:{year}:{organcode or 'no_organcode'}"
    cached_data = redis_client.get(cache_key)

    if cached_data:
        print("cachê - >=2007")
        organs = json.loads(cached_data)
    else:
        print("url - >=2007")
        organs = fetch_organs_tce(tcecode, year, organcode)
        redis_client.setex(cache_key, expiration_time, json.dumps(organs))

    return organs
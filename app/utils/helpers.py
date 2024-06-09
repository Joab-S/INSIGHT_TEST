from app.services.ibge_service import county_mesh_metadata
from app.api.controllers.fetch_ceara_counties_population_siconfi_controller import fetch_ceara_counties_population_by_codibge

def county_response_format(county_id):
    metadata = county_mesh_metadata(county_id)
    basic_info_county = fetch_ceara_counties_population_by_codibge(county_id)
    
    population = basic_info_county["populacao"] if "populacao" in basic_info_county else None
    area = metadata[0]["area"]["dimensao"] if "area" in metadata[0] else None
    population_density = int(population) / float(area) if population is not None and area is not None else None

    return {
        "name":basic_info_county["ente"],
        "area":area,
        "population":population,
        "population_density":population_density,
    }
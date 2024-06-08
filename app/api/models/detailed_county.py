from app.api.models.basic_county import BasicCounty

class DetailedCounty (BasicCounty):
    population_density: float | None = None
    area: str | None = None
    population: int | None = None
    pib: float | None = None
    income_per_capita: float | None = None
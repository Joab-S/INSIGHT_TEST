from fastapi import APIRouter
from app.api.endpoints.get_county import county_router
from app.api.endpoints.get_counties import counties_router
from app.api.endpoints.get_programs import programs_router
from app.api.endpoints.get_program_expenses import programs_expenses_router

api_router = APIRouter()

api_router.include_router(counties_router, prefix="", tags=["Municípios"])
api_router.include_router(county_router, prefix="/counties", tags=["Municípios"])
api_router.include_router(programs_router, prefix="/counties", tags=["Programas"])
api_router.include_router(programs_expenses_router, prefix="/counties", tags=["Programas"])
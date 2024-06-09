from pydantic import BaseModel

class Program (BaseModel):
    cod_program: str
    name: str | None = None
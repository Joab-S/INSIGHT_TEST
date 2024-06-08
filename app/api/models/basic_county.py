from pydantic import BaseModel

class BasicCounty (BaseModel):
    codeibge: int
    name: str
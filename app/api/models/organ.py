from pydantic import BaseModel

class Organ (BaseModel):
    organ_code: str
    organ_name: str
    unit_type_code: str
    organ_cgc: str
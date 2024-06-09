from pydantic import BaseModel

class Function(BaseModel):
    function_code: str
    function_name: str
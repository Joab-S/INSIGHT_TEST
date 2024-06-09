from pydantic import BaseModel

class ProgramExpense(BaseModel):
    program_code: str
    county_code: str
    exercise_budget: int
    org_code: str | None = None
    unit_code: str | None = None
    function_code: str | None = None
    subfunction_code: str | None = None
    code_project_activity: str | None = None
    activity_project_number: str | None = None
    number_subproject_activity: str | None = None
    code_type_budget: str | None = None
    activity_project_name: str | None = None
    description_project_activity: str | None = None
    total_value_fixed_project_activity: float | None = None
from pydantic import BaseModel

class ErrorThrower(BaseModel):
    status_code: int
    message: str
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HealthCheckSchema(BaseModel):
    id: int
    health: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class HealthCheckCreateSchema(BaseModel):
    health: bool

class HealthCheckUpdateSchema(BaseModel):
    id: int
    health: bool
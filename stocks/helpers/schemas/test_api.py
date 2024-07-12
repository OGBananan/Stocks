from pydantic import BaseModel

class TestPostRequest(BaseModel):
    health: bool

class TestPostResponse(BaseModel):
    success: bool

class TestGetResponse(BaseModel):
    latest_health_check: dict  # Assuming this contains the health status and possibly a timestamp

class TestPatchRequest(BaseModel):
    health: bool

class TestPatchResponse(BaseModel):
    success: bool

class TestDeleteResponse(BaseModel):
    success: bool

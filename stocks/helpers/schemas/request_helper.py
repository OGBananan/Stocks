import json
from abc import ABC, abstractmethod
from typing import Type
from pydantic import BaseModel
from django.http import HttpRequest, JsonResponse

class BaseController(ABC):
    def serialize_response(self, response_model: Type[BaseModel], data: dict) -> JsonResponse:
        try:
            response_data = response_model(**data)
            return JsonResponse(response_data.dict())
        except Exception as e:
            raise ValueError(f"Invalid data: {e}")

class PostController(BaseController):
    def serialize_request(self, request: HttpRequest, request_model: Type[BaseModel]) -> BaseModel:
        try:
            data = json.loads(request.body)
            return request_model(**data).dict()
        except Exception as e:
            raise ValueError(f"Invalid data: {e}")
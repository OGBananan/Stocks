from abc import ABC, abstractmethod
from typing import Type
from pydantic import BaseModel
from django.http import HttpRequest, JsonResponse

class BaseController(ABC):
    @abstractmethod
    def handle(self, request: HttpRequest) -> JsonResponse:
        pass

    def serialize_response(self, response_model: Type[BaseModel], data: dict) -> JsonResponse:
        try:
            response_data = response_model(**data)
            return JsonResponse(response_data.dict())
        except Exception as e:
            raise ValueError(f"Invalid data: {e}")

class PostController(BaseController):
    @abstractmethod
    def serialize_request(self, request: HttpRequest, model_cls: Type[BaseModel]) -> BaseModel:
        try:
            data = model_cls(**request.POST.dict())
            return data
        except Exception as e:
            raise ValueError(f"Invalid data: {e}")
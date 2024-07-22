from django.http import JsonResponse
from django.views import View
from .schemas.test_api import (TestPostRequest,
                                TestPostResponse,
                                TestGetResponse,
                                TestPatchRequest,
                                TestPatchResponse,
                                TestDeleteResponse)
from .schemas.request_helper import PostController
from .models import HealthCheck
from asgiref.sync import sync_to_async


class TestHealth(PostController, View):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = lambda _: True
        return view

    async def get(self, request) -> JsonResponse:
        try:
            latest_health = await sync_to_async(HealthCheck.objects.latest)('created_at')
            response_data = TestGetResponse(latest_health_check={
                "health": latest_health.health,
                "timestamp": latest_health.created_at
            })
            return self.serialize_response(TestGetResponse, response_data.dict())
        except HealthCheck.DoesNotExist:
            return JsonResponse({"error": "No health check records found"}, status=404)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

    async def post(self, request) -> JsonResponse:
        try:
            request_data = self.serialize_request(request, TestPostRequest)
            new_health_check = await sync_to_async(HealthCheck.objects.create)(health=request_data.health)
            response_data = TestPostResponse(success=new_health_check.health)
            return self.serialize_response(TestPostResponse, response_data.dict())
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

    async def patch(self, request) -> JsonResponse:
        try:
            request_data = self.serialize_request(request, TestPatchRequest)
            latest_health = await sync_to_async(HealthCheck.objects.latest)('created_at')
            latest_health.health = request_data.health
            await sync_to_async(latest_health.save)()
            response_data = TestPatchResponse(success=latest_health.health)
            return self.serialize_response(TestPatchResponse, response_data.dict())
        except HealthCheck.DoesNotExist:
            return JsonResponse({"error": "No health check records found to update"}, status=404)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

    async def delete(self, request) -> JsonResponse:
        try:
            latest_health = await sync_to_async(HealthCheck.objects.latest)('created_at')
            await sync_to_async(latest_health.delete)()
            response_data = TestDeleteResponse(success=True)
            return self.serialize_response(TestDeleteResponse, response_data.dict())
        except HealthCheck.DoesNotExist:
            return JsonResponse({"error": "No health check records found to delete"}, status=404)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

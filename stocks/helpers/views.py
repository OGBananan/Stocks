import datetime
from django.views import View
from django.http import JsonResponse, HttpRequest
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import HealthCheck
from .schemas.test_api import HealthCheckSchema, HealthCheckCreateSchema, HealthCheckUpdateSchema
from .schemas.request_helper import PostController


@method_decorator(csrf_exempt, name='dispatch')
class TestHealth(PostController, View):

    def get(self, request) -> JsonResponse:
        try:
            latest_health = HealthCheck.objects.latest('created_at').__dict__
            return self.serialize_response(HealthCheckSchema, latest_health)
        except HealthCheck.DoesNotExist:
            return JsonResponse({"error": "No health check records found"}, status=404)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

    def post(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        try:
            health_check_data = self.serialize_request(
                request, HealthCheckCreateSchema)
            if not health_check_data['health']:
                return JsonResponse({"error": "Health check must be true"}, status=400)
            health_check = HealthCheck.objects.create(health=health_check_data['health'],
                                                    created_at=datetime.datetime.now().timestamp(),
                                                    updated_at=datetime.datetime.now().timestamp()
                                                    )
            response_data = model_to_dict(health_check)
            return JsonResponse({"success": "True"}, status=200)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

    def patch(self, request , *args, **kwargs) -> JsonResponse:
        try:
            request_data = self.serialize_request(
                    request,HealthCheckUpdateSchema)
            health_check = HealthCheck.objects.get(id=request_data.get('id'))
            health_check.health = request_data['health']
            health_check.updated_at = datetime.datetime.now().timestamp()
            health_check.save()
            return JsonResponse({"success": True}, status=200)
        except HealthCheck.DoesNotExist:
            return JsonResponse({"error": "No health check records found to update"}, status=404)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

    def delete(self, request) -> JsonResponse:
        try:
            latest_health = HealthCheck.objects.latest('created_at')
            latest_health.delete()
            return JsonResponse({"success": True}, status=204)
        except HealthCheck.DoesNotExist:
            return JsonResponse({"error": "No health check records found to delete"}, status=404)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

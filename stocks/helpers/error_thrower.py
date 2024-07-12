from schemas import error_thrower
from django.http import (
    HttpResponse,
    JsonResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseNotFound,
    HttpResponseServerError,
    HttpResponseGone,
    HttpResponseNotAllowed,
)



def throw_error(status_code, message) -> error_thrower:
    if status_code == 400:
        raise HttpResponseBadRequest(message)
    elif status_code == 403:
        raise HttpResponseForbidden(message)
    elif status_code == 404:
        raise HttpResponseNotFound(message)
    elif status_code == 405:
        raise HttpResponseNotAllowed(message)
    elif status_code == 410:
        raise HttpResponseGone(message)
    elif status_code == 500:
        raise HttpResponseServerError(message)
    else:
        raise HttpResponse(message , status = status_code)

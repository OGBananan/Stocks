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
    HttpResponseConflict,
    HttpResponseUnsupportedMediaType,
    HttpResponseNotImplemented,
    HttpResponseBadGateway,
    HttpResponseServiceUnavailable,
    HttpResponseGatewayTimeout,
)



def throw_error(self) -> error_thrower:
    if self.status_code == 400:
        raise HttpResponseBadRequest(self.message)
    elif self.status_code == 401:
        raise HttpResponseUnauthorized(self.message)  # Replace with appropriate class if needed
    elif self.status_code == 403:
        raise HttpResponseForbidden(self.message)
    elif self.status_code == 404:
        raise HttpResponseNotFound(self.message)
    elif self.status_code == 405:
        raise HttpResponseNotAllowed(self.message)  # Method Not Allowed
    elif self.status_code == 409:
        raise HttpResponseConflict(self.message)
    elif self.status_code == 410:
        raise HttpResponseGone(self.message)
    elif self.status_code == 415:
        raise HttpResponseUnsupportedMediaType(self.message)
    elif self.status_code == 500:
        raise HttpResponseServerError(self.message)
    elif self.status_code == 501:
        raise HttpResponseNotImplemented(self.message)
    elif self.status_code == 502:
        raise HttpResponseBadGateway(self.message)
    elif self.status_code == 503:
        raise HttpResponseServiceUnavailable(self.message)
    else:
        raise HttpResponseServerError(self.message)  # Default to Server Error for unrecognized codes

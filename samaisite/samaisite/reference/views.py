from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

def handle_reference_request(request: WSGIRequest) -> HttpResponse:
    return HttpResponse(content="")

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse

from .inference import first_trial

def handle_inference_request(request: WSGIRequest) -> JsonResponse:
    response = first_trial()
    print(response)
    return JsonResponse(response)

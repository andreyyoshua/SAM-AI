from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .inference import first_trial

@csrf_exempt
def handle_inference_request(request: WSGIRequest) -> JsonResponse:
    response = first_trial(request)
    return JsonResponse(response)

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import glob
from .inference import infer_image

@csrf_exempt
def handle_inference_request(request: WSGIRequest, row: int, column: int) -> JsonResponse:
    response = infer_image(request, row, column)
    return JsonResponse(response)

@csrf_exempt
def handle_file_version_request(request: WSGIRequest) -> JsonResponse:
    path = "./samaisite/static/"
    highest_version = ""
    for file in glob.glob(path + "*.tflite"):
        print(file)
        index = file.index("static\\") + 7
        version = file[index:]
        dot_index = version.index(".tflite")
        version = version[:dot_index]

        if version > highest_version:
            highest_version = version

    url = "http://34.101.215.60/static/" + highest_version + ".tflite"
    return JsonResponse({
        "latest_version": highest_version,
        "file_url": url
    })
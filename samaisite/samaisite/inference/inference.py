from django.core.handlers.wsgi import WSGIRequest
from django.core.files.storage import FileSystemStorage

import time
import numpy as np
from PIL import Image
import torch

from .utils import Bbox

def first_trial(request: WSGIRequest):
    uploaded_image = request.FILES['image']
    if uploaded_image == None:
        return {}
    
    fss = FileSystemStorage()
    file = fss.save(str(time.time()).replace(".", "") + ".png", uploaded_image)
    file_url = "/app" + fss.url(file)

    model = torch.hub.load('/app/samaisite/yolo', 'custom', source='local', path='/app/samaisite/static/best.pt', force_reload=True)

    image = Image.open(file_url)
    width = image.size[0]
    height = image.size[1]

    col = 3
    row = 3
    each_width = width / col
    each_height = height / row
    cells = np.array([])
    for i in range(col):
        for ii in range(row):
            x1 = each_width * i
            y1 = each_height * ii
            x2 = each_width * (i + 1)
            y2 = each_height * (ii + 1)
            box = Bbox(x1, y1, x2, y2, "{} {}".format(i + 1, ii + 1))
            cells = np.append(cells, box)

    results = model(file_url)
    results.pandas().xyxy[0]
    detections = results.pandas().xyxy[0].to_dict(orient="records")

    response = {}
    for detection in detections:
        xMin = detection['xmin']
        yMin = detection['ymin']
        xMax = detection['xmax']
        yMax = detection['ymax']
        for cell in cells:
            box = Bbox(xMin, yMin, xMax, yMax, "")
            isOverlap = cell.isRectangleOverlap(box)
            if isOverlap:
                confidence = detection['confidence']
                _class = detection['class']
                name = detection['name']
                response[name] = cell.label

                break
    
    return response

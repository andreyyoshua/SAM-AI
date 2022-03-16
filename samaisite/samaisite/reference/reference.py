from matplotlib import pyplot as plt
import numpy as np
import cv2
from PIL import Image
import torch
import os

def first_trial():
    model = torch.hub.load('./YOLO/yolov5', 'custom', source='local', path='./YOLO/yolov5/runs/train/exp/weights/best.pt', force_reload=True)
from django.shortcuts import render
import numpy as np
import cv2

def index(request):
    cap = cv2.VideoCapture(0)
    ret, _ = cap.read()
    if ret == True:
        res = "Камера работает"
    else:
        res = "Камера не работает"
    data = {"res": res}
    cv2.destroyAllWindows()
    return render(request, 'mainApp/connecting.html', context=data)

'''
def index(request):
    return render(request, 'mainApp/connecting.html')
'''
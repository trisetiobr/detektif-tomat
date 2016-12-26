import cv2
import numpy as np

def chThresBGR(image, val=0, channel='b'):
    if channel == 'gray':
        _,output = cv2.threshold(image,val,255,cv2.THRESH_BINARY)
        return output
    b,g,r = cv2.split(image)
    if channel == 'b':
        _,output = cv2.threshold(b,val,255,cv2.THRESH_BINARY)
        return output
    elif channel == 'g':
        _,output = cv2.threshold(g,val,255,cv2.THRESH_BINARY)
        return output
    elif channel == 'r':
        r = cv2.subtract(r,g)
        _,output = cv2.threshold(r,val,255,cv2.THRESH_BINARY)
        return output




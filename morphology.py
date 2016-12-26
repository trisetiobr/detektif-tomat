import cv2
import numpy as np

def opening(image,k,i):
    kernel = np.ones((k,k),np.uint8)
    output = cv2.erode(image,kernel,iterations = i)
    output = cv2.dilate(image,kernel,iterations = i)
    return output

def closing(image,k,i):
    kernel = np.ones((k,k),np.uint8)
    output = cv2.dilate(image,kernel,iterations = i)
    output = cv2.erode(image,kernel,iterations = i)
    return output

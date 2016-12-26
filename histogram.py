import cv2
import numpy as np
from matplotlib import pyplot as plt

def histEqualizeAll(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(3,3))
    image[:,:,0] = clahe.apply(image[:,:,0])
    output = cv2.cvtColor(image,cv2.COLOR_YUV2BGR)
    return output

def cmpHist(img,query,ch):
    histQuery = cv2.calcHist([query],[ch],None,[256],[0,256])
    histImg = cv2.calcHist([img],[ch],None,[256],[0,256])
    cv2.normalize(histQuery,histQuery,0,255,cv2.NORM_MINMAX)
    cv2.normalize(histImg,histImg,0,255,cv2.NORM_MINMAX)
    result = cv2.compareHist(histQuery,histImg,cv2.HISTCMP_CORREL)
    print result

def histDraw(image, kelas):
    rows, cols, ch = image.shape
    norm_val = rows*cols
    color = ('B','G','R')
    for i,col in enumerate(color):
        hist = cv2.calcHist([image],[i],None,[256],[0,256])
        hist /= norm_val
        plt.plot(hist,color = col)
        plt.title('Histogram '+ kelas)
        plt.xlim([0,256])
        plt.xlabel('Bin')
        plt.ylabel('P')
    plt.show()

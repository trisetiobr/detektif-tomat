import cv2
import numpy as np
from countfiles import countFiles
from color_average import getAverage
from kelas import saveClass
from classifier import knn
from crop import getRegion

def testing(test_dir):
    k = 7
    n = countFiles(test_dir)
    for i in range(1,n+1):
        img = cv2.imread(test_dir+str(i)+'.jpg')
        #img = getRegion(img)
        data = getAverage(img)
        print('data ke'+str(i))
        output = knn(data,k,1)
        print(output)

test_dir = 'dataset/test/'
testing(test_dir)

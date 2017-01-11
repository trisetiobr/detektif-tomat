import numpy as np
import os, os.path
import cv2
import csv
import math
from operator import itemgetter
from histogram import histEqualizeAll
from kelas import saveClass, loadClass, loadDataTrain

def knn(data,k,process):
    dataTrain = loadDataTrain()
    result = []
    for i in dataTrain[1:]:
        euclidian = 0
        #menghitung jarak euclidian
        for j in range(0,len(i)-1):
            euclidian += abs(float(data[j]) - float(i[j]))**2
        euclidian = (i[-1],round((math.sqrt(euclidian))))
        result.append(euclidian)
    result.sort(key=itemgetter(1))
    #voting
    n = 0
    most = 0
    kelas = loadClass()
    output = []
    for j in range(0,len(kelas[0])):
        for i in result[:k]:
            if i[0] == kelas[0][j]:
                n += 1
        if n >= most:
            most = n
            output = [kelas[0][j],most]
        n = 0
    if process == 0:
        return output[0]
    else:
        print('Klasifikasi KNN, dengan k = ' + str(k))
        print('(tingkat kematangan, jarak euclidian)')
        for i in (result[:k]):
            print(i)
        return output[0]



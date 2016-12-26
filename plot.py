import numpy as np
import cv2
import math
from kelas import saveClass, loadClass, loadDataTrain
import matplotlib as plt

def plotGraph():
    kelas = loadClass()
    dataTrain = loadDataTrain()
    #plt.plot(dataTrain[0][:1])
    print(dataTrain)

plotGraph()    

import numpy as np
import cv2
import argparse

from operator import itemgetter
from histogram import histEqualizeAll
from kelas import saveClass, loadClass, loadDataTrain, loadInput, saveOutput
from classifier import knn
from color_average import getAverage
from output import showOutput


def inputImage(input_directory,process=1):
    k = 7
    img = cv2.imread(input_directory)
    img = histEqualizeAll(img)
    output = knn(getAverage(img),k,process)
    cv2.imshow('citra tomat', img)
    print('tingkat kematangan citra tomat yang anda masukkan: ' + output)
    cv2.waitKey(0)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

inputImage(args["image"])


import cv2
import numpy as np
import csv
from preprocess import preProcess
from countfiles import countFiles
from color_average import getAverage
from kelas import saveClass

def runPreprocess():   
    preProcess('dataset/unproses/test/')
    preProcess('dataset/unproses/train/mentah/')
    preProcess('dataset/unproses/train/setengah-matang/')
    preProcess('dataset/unproses/train/matang/')

def training(train_dir,data):
    for i in train_dir:
        n = countFiles(i)
        kelas = i.split('/')
        for j in range(1,n+1):
            img = cv2.imread(i+str(j)+'.jpg')
            value = getAverage(img)
            value.append(kelas[-2])
            data.append(value)
    with open('dataset/train.csv','wb')as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

train_dir = ['dataset/train/mentah/','dataset/train/setengah-matang/','dataset/train/matang/']
data = [['h','s','v','kelas']]
runPreprocess()
training(train_dir,data)
saveClass(train_dir)

import cv2
from countfiles import countFiles
from color_average import getAverage
from histogram import histEqualizeAll

def preProcess(open_dir):
    n = countFiles(open_dir)
    folder_name = open_dir.split('/')
    if folder_name[-3] == 'train':
        save_dir = 'dataset/train/'+folder_name[-2]+'/'
    else:
        save_dir = 'dataset/'+folder_name[-2]+'/'
    print(save_dir)
    for i in range(1,n+1):
        img = cv2.imread(open_dir+str(i)+'.jpg')
        img = histEqualizeAll(img)
        cv2.imwrite(save_dir+str(i)+'.jpg',img)

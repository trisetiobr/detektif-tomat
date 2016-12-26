import csv

def saveClass(class_dir):
    kelas = []
    for i in class_dir:
        class_name = i.split('/')
        kelas.append(class_name[-2])
    with open('dataset/class.csv','wb')as csvfile:
        writer = csv.writer(csvfile, delimiter=',',lineterminator='\n')
        writer.writerow(kelas)
        
def loadClass():
    with open('dataset/class.csv','rb') as csvfile:
        reader = csv.reader(csvfile)
        dataClass = list(reader)
    return dataClass

def loadInput():
    with open('pic/input.csv','rb') as csvfile:
        reader = csv.reader(csvfile)
        dataClass = list(reader)
    return dataClass

def saveOutput(data):
    with open('pic/output.csv','wb')as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

def loadOutput():
    with open('pic/output.csv','rb') as csvfile:
        reader = csv.reader(csvfile)
        output = list(reader)
    return output
           
def loadDataTrain():
    with open('dataset/train.csv','rb') as csvfile:
        reader = csv.reader(csvfile)
        dataTrain = list(reader)
    return dataTrain

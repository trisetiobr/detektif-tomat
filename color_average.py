import numpy as np

def getAverage(image):
    average_color_per_row = np.average(image, axis = 0)
    average_color = np.round(np.average(average_color_per_row, axis = 0))
    output = [average_color[0], average_color[1], average_color[2]]
    return output

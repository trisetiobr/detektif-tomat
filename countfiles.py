import os, os.path

def countFiles(directory):
    counter = 0
    for _, dirnames, filenames, in os.walk(directory):
        counter += len(filenames)
    return counter

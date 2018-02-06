from PIL import Image
import numpy as np
import png
import matplotlib.pyplot as plt


def quanTable(b, q):
    table = [0 for i in range(b)]
    for i in range(b):
        table[i] = int(i/q)
    return table


def uniformQuan(imageLocation, level):
    # Read a image and convert it to gray scale image as an array
    Ima = np.array(Image.open(imageLocation).convert('L'))
    [height, width] = Ima.shape
    b = 256
    q = b/level
    qTable = quanTable(b, q)
    qImg = [[0 for i in range(width)] for j in range(height)]
    for i in range(height):
        for j in range(width):
            qImg[i][j] = qTable[int(Ima[i][j])]
    return np.array(qImg)


def main(inputRoute, outputRoute, level = 2):
    result = uniformQuan(inputRoute, level)
    bitdepth = 1
    while level > 2:
        level = level/2
        bitdepth = bitdepth+1
    f = open(outputRoute, 'wb')
    w = png.Writer(len(result[0]), len(result), greyscale=True, bitdepth=bitdepth)
    w.write(f, result)
    f.close()


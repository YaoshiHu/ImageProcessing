from PIL import Image
import numpy as np
import png


def noiseMatrix(height, width, q):
    noise = [[0 for i in range(width)] for j in range(height)]
    for i in range(height):
        for j in range(width):
            noise[i][j] = np.random.uniform(-q/2, q/2)
    return np.array(noise)


def quanTable(b, q, min):
    table = [0 for i in range(b)]
    for i in range(b):
        table[i] = int(i/q)*q+q/2+min
    return table


def noiseQuan(imageLocation, level):
    # Read a image and convert it to gray scale image as an array
    Ima = np.array(Image.open(imageLocation).convert('L'))
    [height, width] = Ima.shape
    maximum = 255
    minimum = 0
    b = maximum - minimum + 1
    q = b/level
    noise = noiseMatrix(height, width, q)
    qTable = quanTable(b, q, minimum)
    qImg = [[0 for i in range(width)] for j in range(height)]
    for i in range(height):
        for j in range(width):
            qImg[i][j] = int((qTable[int(max(min(maximum, noise[i][j] + Ima[i][j]), minimum)-minimum)] - noise[i][j])/q)
    return qImg


def main(inputRoute, outputRoute, level = 2):
    result = noiseQuan(inputRoute, level)
    bitdepth = 1
    while level > 2:
        level = level/2
        bitdepth = bitdepth+1
    f = open(outputRoute, 'wb')
    w = png.Writer(len(result[0]), len(result), greyscale=True, bitdepth=bitdepth)
    w.write(f, result)
    f.close()

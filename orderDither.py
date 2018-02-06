from PIL import Image
import numpy as np
import math
import png


# define a copy of a matrix
def copyMatrix(object):
    # if input is a vector
    if type(object[0]) != list:
        result = []
        for ele in object:
            result.append(ele)
        return result
    # input is a matrix
    else:
        result = [[0 for i in range(len(object[0]))] for j in range(len(object))]
        for i in range(len(object)):
            for j in range(len(object[0])):
                result[i][j] = object[i][j]
        return result


# input the pattern order
def pattern(order):
    origin = [[0, 2], [3, 1]]
    i = 1
    while i < order:
        # compute 4 times the original matrix which will be used
        for i in range(len(origin)):
            for j in range(len(origin[0])):
                origin[i][j] *= 4
        upperLeft = copyMatrix(origin)
        upperRight = copyMatrix(origin)
        bottomLeft = copyMatrix(origin)
        bottomRight = copyMatrix(origin)
        for i in range(len(origin)):
            for j in range(len(origin[0])):
                upperRight[i][j] += 2
                bottomLeft[i][j] += 3
                bottomRight[i][j] += 1
        upper = []
        bottom = []
        for i in range(len(origin)):
            upper.append(upperLeft[i]+upperRight[i])
            bottom.append(bottomLeft[i]+bottomRight[i])
        origin = upper+bottom
        i += 1
    return np.array(origin)


def orderDither(Img, patternOrder):
    pttn = pattern(patternOrder)
    # pttnLen is the length of the matrix we derive
    pttnLen = int(math.pow(2, patternOrder))
    # level is the grayscale can be represented
    level = pttnLen * pttnLen
    result = [[0 for i in range(len(Img[0]))] for j in range(len(Img))]
    for i in range(len(Img)):
        for j in range(len(Img[0])):
            value = 1 if Img[i][j] > 256 * pttn[i % pttnLen][j % pttnLen] / level else 0
            result[i][j] = value
    return result


def main(inputRoute, outputRoute, patternOrder=3):
    Img = np.array(Image.open(inputRoute).convert('L'))
    [height, width] = Img.shape
    result = orderDither(Img, patternOrder)
    f = open(outputRoute, 'wb')
    w = png.Writer(width, height, greyscale=True, bitdepth=1)
    w.write(f, result)
    f.close()

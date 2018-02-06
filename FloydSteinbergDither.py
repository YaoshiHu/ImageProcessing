from PIL import Image
import numpy as np
import png


# weight of bottom is 3/8
# weight of right is 3/8
# weight of bottom right is 2/8
def quanImg(img, level):
    [height, width] = img.shape
    result = [[0 for i in range(width)] for j in range(height)]
    qtable = quantable(256, level)
    q = 256/level
    for i in range(height):
        for j in range(width):
            tmp = result[i][j]
            result[i][j] = qtable[int(img[i][j])]
            error = tmp - result[i][j]
            if i < height-1 and j < width-1:
                tmp = min(max(result[i+1][j+1]+error/4, 0), 255)
                result[i+1][j+1] = tmp

            if i < height-1:
                tmp = min(max(result[i+1][j]+3*error/8, 0), 255)
                result[i+1][j] = tmp

            if j < width-1:
                tmp = min(max(result[i][j+1]+3*error/8, 0), 255)
                result[i][j+1] = tmp
    for i in range(height):
        for j in range(width):
            result[i][j] = int(result[i][j]/q)
    return np.array(result)


# a function to create a quantable
# Create the quantization table, b is the bin, l is the level, min is the minimum value, rng is the range of the input
def quantable(b, l, min=0):
    q = b / l
    table = [0 for i in range(b)]
    for i in range(b):
        table[i] = int(i / q) * q + q / 2 + min
    return table


def main(inputRoute, outputRoute, level=2):
    img = np.array(Image.open(inputRoute).convert('L'))
    result = quanImg(img, level)
    bitdepth = 1
    while level > 2:
        level = level / 2
        bitdepth = bitdepth + 1
    f = open(outputRoute, 'wb')
    w = png.Writer(len(result[0]), len(result), greyscale=True, bitdepth=bitdepth)
    w.write(f, result)
    f.close()

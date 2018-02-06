from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# weight of bottom is 3/8
# weight of right is 3/8
# weight of bottom right is 2/8
def quanImg(img, qtable):
    [height, width] = img.shape
    result = [[0 for i in range(width)] for j in range(height)]
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
    return result


# a function to create a quantable
# Create the quantization table, b is the bin, l is the level, min is the minimum value, rng is the range of the input
def quantable(b, l, min=0):
    q = b / l
    table = [0] * b
    for i in range(b):
        table[i] = int(i / q) * q + q / 2 + min
    return table


def fsDitherQuan(inputRoute, outputRoute, outputDPI=300, level=2):
    img = np.array(Image.open(inputRoute).convert('L'))
    plt.figure()
    qtable = quantable(256, level)
    result = quanImg(img, qtable)
    result = np.array(result)
    plt.imshow(result, cmap=plt.cm.gray)
    plt.axis('off')
    plt.title('Level ' + str(level) + " Floyed Steinberg Dither Quantized image")
    plt.savefig(outputRoute, dpi=outputDPI)


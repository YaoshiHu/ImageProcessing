from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def quanImg(img, qtable):
    [height, width] = img.shape
    result = [[0 for i in range(width)] for j in range(height)]
    for i in range(height):
        for j in range(width):
            result[i][j] = qtable[int(img[i][j])]
    return result


# a function to create a quantable
# Create the quantization table, b is the bin, l is the level, min is the minimum value, rng is the range of the input
def quantable(b, l, min=0):
    q = b / l
    table = [0] * b
    for i in range(b):
        table[i] = int(i / q) * q + q / 2 + min
    return table


# create a noise matrix with height = m and width = n
def noiseCreate(b, l, m, n):
    noise = [[0 for i in range(n)] for j in range(m)]
    q_2 = b/l/2
    for i in range(m):
        for j in range(n):
            noise[i][j] = np.random.uniform(-q_2, q_2)
    return np.array(noise)


# adding or canceling noise, if flag = 0, it is adding noise, otherwise, it is subtracting noise
def addNoise(img, noise, flag=0):
    if flag == 0:
        for i in range(len(noise)):
            for j in range(len(noise[0])):
                value = int(img[i][j] + noise[i][j])
                if value < 0:
                    value = 0
                if value > 255:
                    value = 255
                img[i][j] = value
    else:
        for i in range(len(noise)):
            for j in range(len(noise[0])):
                value = int(img[i][j] - noise[i][j])
                if value < 0:
                    value = 0
                if value > 255:
                    value = 255
                img[i][j] = value
    img = np.array(img)
    return img


def uniformQuan(inputRoute, outputRoute, outputDPI=300, level=2):
    img = np.array(Image.open(inputRoute).convert('L'))
    [height, width] = img.shape
    plt.figure()
    qtable = quantable(256, level)
    result = quanImg(img, qtable)
    result = np.array(result)
    plt.imshow(result, cmap=plt.cm.gray)
    plt.axis('off')
    plt.title('Level ' + str(level) + " uniform Quantized image")
    plt.savefig(outputRoute, dpi=outputDPI)


def noiseQuan(inputRoute, outputRoute, outputDPI=300, level=2):
    img = np.array(Image.open(inputRoute).convert('L'))
    [height, width] = img.shape
    plt.figure()
    qtable = quantable(256, level)
    noise = noiseCreate(256, level, height, width)
    img = addNoise(img, noise, 0)
    result = quanImg(img, qtable)
    result = np.array(result)
    plt.imshow(result, cmap=plt.cm.gray)
    plt.axis('off')
    plt.title('Level ' + str(level) + " noise Quantized image")
    plt.savefig(outputRoute, dpi=outputDPI)



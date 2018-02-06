from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


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
    maximum = np.max(Ima)
    minimum = np.min(Ima)
    b = maximum - minimum + 1
    q = b/level
    noise = noiseMatrix(height, width, q)
    qTable = quanTable(b, q, minimum)
    qImg = [[0 for i in range(width)] for j in range(height)]
    MSE = 0
    for i in range(height):
        for j in range(width):
            qImg[i][j] = qTable[int(max(min(maximum, noise[i][j] + Ima[i][j]), minimum)-minimum)] - noise[i][j]
            MSE += (Ima[i][j]-qImg[i][j]) ** 2
    MSE = MSE / (height*width)
    return qImg, MSE


level = [64, 32, 16, 8]
plt.figure()
for i in range(len(level)):
    result, mse = noiseQuan("./Einstein.jpg", level[i])
    result = np.array(result)
    plt.subplot(221+i)
    plt.imshow(result, cmap=plt.cm.gray)
    plt.axis('off')
    plt.title('Level ' + str(level[i]) + ' image with MSE ' + str(mse))
    print "Under level "+str(level[i])+", the MSE of the quantized image is "+str(mse)
plt.show()


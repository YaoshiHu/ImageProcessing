from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def quanTable(b, q, min):
    table = [0 for i in range(b)]
    for i in range(b):
        table[i] = int(i/q)*q+q/2+min
    return table


def uniformQuan(imageLocation, level):
    # Read a image and convert it to gray scale image as an array
    Ima = np.array(Image.open(imageLocation).convert('L'))
    [height, width] = Ima.shape
    maximum = np.max(Ima)
    minimum = np.min(Ima)
    b = maximum - minimum + 1
    q = b/level
    qTable = quanTable(b, q, minimum)
    qImg = [[0 for i in range(width)] for j in range(height)]
    MSE = 0
    for i in range(height):
        for j in range(width):
            qImg[i][j] = qTable[int(Ima[i][j])]
            MSE += 1.0*(Ima[i][j]-qImg[i][j]) ** 2
    MSE = MSE / (height*width)
    return qImg, MSE


level = [64, 32, 16, 8]
plt.figure()
for i in range(len(level)):
    result, mse = uniformQuan("./Einstein.jpg", level[i])
    result = np.array(result)
    plt.subplot(221+i)
    plt.imshow(result, cmap=plt.cm.gray)
    plt.axis('off')
    plt.title('Level ' + str(level[i]) + ' image with MSE ' + str(mse))
    # print "Under level "+str(level[i])+", the MSE of the quantized image is "+str(mse)
plt.show()


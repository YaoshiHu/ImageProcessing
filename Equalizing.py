from PIL import Image
import numpy as np
import png


def hist(img):
    height, width = img.shape
    pixelnum = height * width
    # Compute the normalized histogram (original image)
    histogram = [0.0 for i in range(256)]
    for i in range(height):
        for j in range(width):
            histogram[img[i, j]] += 1
    for i in range(256):
        histogram[i] /= pixelnum
    return histogram


def mapping(histogram):
    m = [0.0 for i in range(256)]
    for i in range(1, 255):
        m[i] = m[i-1]+histogram[i]
    for i in range(0, 255):
        m[i] = int(m[i]*255)
    return m


def generating(img, histogram):
    m = mapping(histogram)
    height, width = img.shape
    result = np.zeros((height, width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            result[i][j] = m[img[i][j]]
    return result


def main(imgDirc, outputRoute):
    img = np.array(Image.open(imgDirc))
    hist1 = hist(img)
    result = generating(img, hist1)
    f = open(outputRoute, 'wb')
    w = png.Writer(len(result[0]), len(result), greyscale=True, bitdepth=8)
    w.write(f, result)
    f.close()
    # hist2 = hist(result)


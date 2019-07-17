# BEGIN.

import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

os.chdir('c:\src\opencv')

# Configuration: 

# Number of pixels in down-sized image if possible:
TARGET_NUM_PIXELS = 1024 * 1024

# Read original image.
gray = cv2.imread('sudoku1.jpg', cv2.IMREAD_GRAYSCALE)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print gray.shape, gray.size

(w, h) = gray.shape
actual_pixels = w * h

print actual_pixels, TARGET_NUM_PIXELS

scale = math.sqrt( actual_pixels / TARGET_NUM_PIXELS )

print scale

dim = (int(w / scale), int(h / scale))

resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)
resized = cv2.medianBlur(resized, 5)

print resized.shape, resized.size

blur = cv2.GaussianBlur(resized,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


# thresh = cv2.adaptiveThreshold(resized, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                               cv2.THRESH_BINARY, 11, 2)

# kernel = np.ones((5,5), np.uint8)
# erode = cv2.erode(thresh, kernel, iterations = 1)
#cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

plt.imshow(cv2.cvtColor(th3, cv2.COLOR_BGR2RGB)),plt.show()

# END.

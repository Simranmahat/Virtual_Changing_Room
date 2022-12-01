import cv2
import numpy as np
import skimage.exposure

img = cv2.imread('objects/glass.png')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = (40, 50, 50)
upper = (100, 255, 255)
mask = cv2.inRange(img_hsv, lower, upper)
mask = 255 - mask

kernel = np.ones((3, 3), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

result = img.copy()
result[mask == 0] = (255, 255, 255)

mask = cv2.GaussianBlur(mask, (0, 0), sigmaX=3, sigmaY=3, borderType=cv2.BORDER_DEFAULT)
mask = skimage.exposure.rescale_intensity(mask, in_range=(127.5, 255), out_range=(0, 255))
result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
result[:, :, 3] = mask


cv2.imwrite('outputs/result.png', result)





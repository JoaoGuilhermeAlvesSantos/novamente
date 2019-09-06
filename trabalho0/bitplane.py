import numpy as np
import cv2 
img = cv2.imread("varus.jpg", cv2.IMREAD_GRAYSCALE)

i = int(input())
for _ in range(i):
    img = img >> 1
img = (img & 1)

cv2.imshow("baboon", img*255)


cv2.waitKey(0)
cv2.destroyAllWindows()


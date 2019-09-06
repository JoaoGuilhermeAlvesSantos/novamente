import numpy as np
import cv2


im1 = cv2.imread('baboon.png')
im2 = cv2.imread('butterfly.png')

im = np.uint8(im1*0.5 + im2*0.5)  
cv2.imshow("Sombra1", im)

im = np.uint8(im1*0.2 + im2*0.8)  
cv2.imshow("Sombra2", im)

im = np.uint8(im1*0.8 + im2*0.2)  
cv2.imshow("Sombra3", im)


cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2 

# Load an color image in grayscale
img = cv2.imread('varus.jpg',0)
img_not = cv2.bitwise_not(img)

cv2.imshow('image',img)
cv2.imshow('imageneg',img_not)
cv2.imwrite('varusnegativo.png',img_not)
cv2.imwrite('varuspretoebranco.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



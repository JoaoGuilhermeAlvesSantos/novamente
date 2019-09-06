import numpy as np
import cv2 

# Load an color image in grayscale
img = cv2.imread('varus.jpg',cv2.IMREAD_COLOR)
norm_image = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
alfa = 1
norm_image = norm_image**(1/alfa)


norm_image = np.uint8(norm_image*255)

cv2.imshow("varusbrilho", norm_image)
cv2.imwrite("Varuscinza.jpg", norm_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


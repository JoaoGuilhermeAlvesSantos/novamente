import numpy as np
import cv2 

def FloydSteinberg(f):
    height, width = f.shape
    g = np.ones((height, width), dtype = "float32")
    
    f = cv2.normalize(f, None, alpha=0, beta=1, norm_type= cv2.NORM_MINMAX, dtype= cv2.CV_32F)
    
    for y in range(0, height - 1):
        for x in range(1, width - 1):
            if f[y, x] < 0.5:
                g[y, x] = 0
            else:
                g[y, x] = 1
            erro = f[y, x] - g[y, x]
            f[y, x+1] = f[y, x+1] + (7/16)*erro 
            f[y+1, x-1] = f[y+1, x-1] + (3/16)*erro
            f[y+1, x] = f[y+1, x] + (5/16)*erro
            f[y+1, x+1] =  f[y+1, x+1] + (1/16)*erro
    return np.uint8(g)


img = cv2.imread("varus.jpg", 0) 
im2 = FloydSteinberg(img)


cv2.imwrite("FloydSteinberggray.jpg", im2*255)


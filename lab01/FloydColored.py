import numpy as np
import cv2 

def FloydSteinberg(f):
    g = np.copy(f)
    height, width, channels = f.shape
    for z in range(channels):
        for x in range(1, width - 1):
            
            for y in range(0, height - 1):          
                if f[y, x, z] < 128:
                    g[y, x, z] = 0
                else:
                    g[y, x, z] = 1
                erro = f[ y, x, z] - g[ y, x, z]*255
                f[y+1, x,  z] = f[y+1, x, z] + (7/16)*erro 
                f[y-1, x+1,  z] = f[y-1, x+1, z] + (3/16)*erro
                f[y, x+1, z] = f[y, x+1, z] + (5/16)*erro
                f[y+1, x+1, z] =  f[y+1, x+1, z] + (1/16)*erro
    return np.uint8(g)

img = cv2.imread("baboon.png") 
im2 = FloydSteinberg(img)

cv2.imwrite("FloydSteinbergcolored.png", im2*255)


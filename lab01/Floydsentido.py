import numpy as np
import cv2 



def FloydSteinberg(f):
    g = np.copy(f)
    height, width= f.shape
    for x in range(1, width - 1):
        if x&1:
            for y in range(0, height - 1):          
                if f[y, x] < 128:
                    g[y, x] = 0
                else:
                    g[y, x] = 1
                erro = f[ y, x] - g[ y, x]*255
                f[y+1, x] = f[y+1, x] + (7/16)*erro 
                f[y-1, x+1] = f[y-1, x+1] + (3/16)*erro
                f[y, x+1] = f[y, x+1] + (5/16)*erro
                f[y+1, x+1] =  f[y+1, x+1] + (1/16)*erro
        else:
            for y in range(height - 2, 0, -1):
                if f[y, x] < 128:
                    g[y, x] = 0
                else:
                    g[y, x] = 1
                erro = f[y, x] - g[y, x]*255
                f[y-1, x] = f[y-1, x] + (7/16)*erro 
                f[y-1, x+1] = f[y-1, x+1] + (1/16)*erro
                f[y, x+1] = f[y, x+1] + (5/16)*erro
                f[y+1, x+1] =  f[y+1, x+1] + (3/16)*erro
    return np.uint8(g)


img = cv2.imread("varus.jpg", 0) 
im2 = FloydSteinberg(img)

cv2.imwrite("Floydgrayzigzag.jpg", im2*255)




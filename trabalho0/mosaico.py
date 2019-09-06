import numpy as np
import cv2
def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv2.vconcat(im_list_resize)

def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv2.hconcat(im_list_resize)

im = cv2.imread('baboon.png')
col = im.shape[0]
lin = im.shape[1]

img = []

for i in range(0, col, int(col/4)):
    for j in range(0, lin, int(lin/4)):
        img.append( im[i : int(i +  col/4) , j: int(j + lin/4)] )


im_v1 = vconcat_resize_min([img[5], img[7], img[11], img[3]])
im_v2 = vconcat_resize_min([img[10], img[15], img[13], img[14]])
im_v3 = vconcat_resize_min([img[12], img[0], img[1], img[9]])
im_v4 = vconcat_resize_min([img[2], img[8], img[6], img[4]])

im_h = hconcat_resize_min([im_v1, im_v2, im_v3, im_v4])
cv2.imshow("cropped", im_h)
cv2.waitKey(0)
cv2.destroyAllWindows()

# -*- coding: utf-8 -*-
import cv2

img = cv2.imread("noob.jpg")
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

img_rbb = cv2.merge([r,b,b])
cv2.imshow("RBB",img_rbb)
#cv2.imshow("opencv02",img)
#cv2.imshow("blue",b)
#cv2.imshow("green",g)
#cv2.imshow("red",r)

cv2.waitKey(0)
 
#cv2.destroyAllwindows()  
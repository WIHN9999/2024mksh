# -*- coding: utf-8 
import cv2

img = cv2.imread("noob.jpg")
b = img[:,:,0]
print(b)
cv2.imshow("opencv06",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
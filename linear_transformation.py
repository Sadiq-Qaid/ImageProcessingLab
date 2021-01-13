#	Scaling:

import cv2 as c
import numpy as np
img= cv2.imread("app.jpg")
h,w=img.shape[0:2]
width=int(w*1)
hight=int(h*1)
dim =(width,hight)
res=c.resize(img,dim)
c.imshow("Scaling",res)
c.waitKey(0)
c.destroyAllWindows()


b.	Rotation:
import cv2 as c
import numpy as np
img= cv2.imread("app.jpg")
h,w=img.shape[0:2]
rotationMatrix=cv2.getRotationMatrix2D((w/2,h/2),90,.5)
rotated_img=cv2.warpAffine(img,rotationMatrix,(w,h))
c.imshow("Orignal_Image",img)
c.imshow("rotation",rotated_img)
c.waitKey(0)
c.destroyAllWindows()

# program to display grayscale image using read and write operations
# Description:grayscale
# Grayscaling is the process of converting an image from other color spaces e.g RGB, CMYK, HSV, etc. to shades of gray. It varies between complete black and complete white.

#Importance of grayscaling –

#Dimension reduction: For e.g. In RGB images there are three color channels and has three dimensions while grayscaled images are single dimensional. Reduces model complexity: Consider training neural article on RGB images of 10x10x3 pixel.The input layer will have 300 input nodes. On the other hand, the same neural network will need only 100 input node for grayscaled images. For other algorithms to work: There are many algorithms that are customized to work only on grayscaled images e.g. Canny edge detection function pre-implemented in OpenCV library works on Grayscaled images only.

import cv2
img= cv2.imread("app.jpg")
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("opencv-greyscale.png",gray_image)
cv2.imshow("Orignal",img)
cv2.imshow("Gray_Scale",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#program to perform a linear transformation for an image (scaling & rotation)
# Description: scaling
   #When we are programming with OpenCV in Python, we often need images with specific dimensions. For example, let’s suppose that we want to resize a large image to fit on our computer screen and we need to shrink it. So, how we can do that?

#We already learned that a digital image is presented in our computer by a matrix of pixels and each pixel has a specific value. So, if we want to resize our image, we just need to multiply values of our pixels with some scalar. In order to do that we just need to define coordinates of our resized image and apply function cv2.resize(). So, let’s see how it works:
# a. scaling
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


# b.	Rotation:
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


# program to find sum and mean of a set of images
import cv2
import os
path='D:\images'
imgs = []
files = os.listdir(path)
for file in files:
    filepath=path+"\\"+file
    imgs.append(cv2.imread(filepath))
i=0
im = []
for im in imgs:
    #cv2.imshow(files[i], imgs[i])
    im+=imgs[i]
    i = i +1
cv2.imshow("Sum_OF_FOUR_IMAGES",im)
meanImg = im/len(files)
cv2.imshow("MEAN_OF_FOUR_IMAGES",meanImg)
cv2.waitKey(0)

# program to convert image into a binary (Black and white) colour.
import cv2
img = cv2.imread('cat.jpg',2)
ret, bw_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("Orignal_Image",img)
cv2.imshow("Binary Image",bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# program to convert the given colour image to different colour spaces.
import cv2
image = cv2.imread('cat.jpg')
img_HLS = cv2.cvtColor(image,cv2.COLOR_BGR2HLS)
img_HSV = cv2.cvtColor(image,cv2.cv2.COLOR_BGR2HSV)
img_RGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) 
cv2.imshow("original", image) 
cv2.imshow("HLS", img_HLS)  
cv2.imshow("HSV", img_HSV)
cv2.imshow("RGB", img_RGB)
cv2.waitKey(0) 
cv2.destroyAllWindows()


# program to create an image from 2D array (create an array of random size and density values).

import numpy
from PIL import Image
imarray = numpy.random.rand(512,512,3) * 255
imarray[0:512,0:512] = [100,0,255]
im = Image.fromarray(imarray,'RGB')
im.save('Generated_Image.jpg')
im.show()

# Assignment:	
   # 1. Develop a program to find the neighbours of each element in the matrix.
   # 2. Write a program to find the sum of neighbour values in a matrix.


# 4 and 8 Neighburs
import numpy as np
axis = int(input("Enter the radius of the matrix:"))
neighbor = int(input("Enter the 4 or 8 to calculate the neighbors"))

if neighbor == 4 or neighbor == 8:
    x =np.empty((axis,axis))
    y = np.empty((axis+2,axis+2))
    s =np.empty((axis,axis))
    
    # Generating the Values of the Matrix
    for i in range(0,axis):
        for j in range(0,axis):
            x[i][j]=int(i+j+1)
    for i in range(0,axis):
        for j in range(0,axis):
            print(int(x[i][j]),end = '\t')
        print('\n')


    for i in range(0,axis+2):
        for j in range(0,axis+2):
            if i == 0 or i == axis+1 or j == 0 or j==axis+1:
                y[i][j]=0
            else:
                y[i][j]=x[i-1][j-1]
    for i in range(0,axis+2):
        for j in range(0,axis+2):
            print(int(y[i][j]),end = '\t')
        print('\n')

    for i in range(0,axis):
        for j in range(0,axis):
            if neighbor == 4:                
                s[i][j]=((y[i][j+1]+y[i+1][j]+y[i+1][j+2]+y[i+2][j+1]))
                print(x[i][j],":",end = '\t')
                print(y[i][j+1],',',y[i+1][j],',',y[i+1][j+2],',',y[i+2][j+1])
                #print(s[i][j],end = '\t')
            elif neighbor ==8:
                    s[i][j]=((y[i][j]+y[i][j+1]+y[i][j+2]+y[i+1][j]+y[i+1][j+2]+y[i+2][j]+y[i+2][j+1]+y[i+2][j+2]))
                    print(x[i][j],":",end = '\t')
                    print(y[i][j],',',y[i][j+1],',',y[i][j+2],',',y[i+1][j],',',y[i+1][j+2],',',y[i+2][j],',',y[i+2][j+1],',',y[i+2][j+2])
                    #print(s[i][j],end = '\t')
        print('\n')
else:
     print("Wrong neighbors, you have to select ether 4 or 8")

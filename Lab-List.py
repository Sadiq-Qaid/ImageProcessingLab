# program to display grayscale image using read and write operations
# Description:grayscale
# Grayscaling is the process of converting an image from other color spaces e.g RGB, CMYK, HSV, etc. to shades of gray.
#It varies between complete black and complete white.

#Importance of grayscaling –

# Dimension reduction: For e.g. In RGB images there are three color channels and has three dimensions while grayscaled images are single dimensional.
# Reduces model complexity: Consider training neural article on RGB images of 10x10x3 pixel.The input layer will have 300 input nodes.
# On the other hand, the same neural network will need only 100 input node for grayscaled images.
# For other algorithms to work: There are many algorithms that are customized to work only on grayscaled images
#e.g. Canny edge detection function pre-implemented in OpenCV library works on Grayscaled images only.

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
#When we are programming with OpenCV in Python, we often need images with specific dimensions.
#For example, let’s suppose that we want to resize a large image to fit on our computer screen and we need to shrink it. So, how we can do that?
#We already learned that a digital image is presented in our computer by a matrix of pixels and each pixel has a specific value.
#So, if we want to resize our image, we just need to multiply values of our pixels with some scalar.
#In order to do that we just need to define coordinates of our resized image and apply function cv2.resize(). So, let’s see how it works:

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


# b. Rotation:
# description
# When we perform rotation in linear algebra we always rotate along the center of the coordinate system, However,
#in OpenCV while processing images we can also rotate our image along arbitrary point which can be defined as an additional parameter of our function.
#For instance, very often this parameter can be a center of the image and it will be defined in the following way.
#After defining a rotation matrix M we need to call cv2.getRotationMatrix2D() function which has few arguments.
#The first argument is the point around which we want to rotate the image, in our case it will be the center.
#Finally, we can apply the rotation to our image using cv2.warpAffine()method.
# We need to specify our rotation matrix M and the height and the width of our output image.


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
# Description:
#In digital image processing, the sum of absolute differences (SAD) is a measure of the similarity between image blocks.
#It is calculated by taking the absolute difference between each pixel in the original block and the corresponding pixel in the block being used for comparison
#Mean is most basic of all statistical measure. Means are often used in geometry and analysis;
#a wide range of means have been developed for these purposes.
#In contest of image processing filtering using mean is classified as spatial filtering and used for noise reduction.

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

#Binary images are images whose pixels have only two possible intensity values. Numerically,
#the two values are often 0 for black, and either 1 or 255 for white.
#The main reason binary images are particularly useful in the field of Image Processing is because they allow easy separation of an object from the background.
#In digital photography, computer-generated imagery, and colorimetry,
#a grayscale or image is one in which the value of each pixel is a single sample representing only an amount of light;
#that is, it carries only intensity information Grayscale images, a kind of black-and-white or gray monochrome, are composed exclusively of shades of gray.


import cv2
img = cv2.imread('cat.jpg',2)
ret, bw_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("Orignal_Image",img)
cv2.imshow("Binary Image",bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# program to convert the given colour image to different colour spaces.
#Description:
#Color spaces are different types of color modes, used in image processing and signals and system for various purposes.
#The color spaces in image processing aim to facilitate the specifications of colors in some standard way.
#Different types of color spaces are used in multiple fields like in hardware, in multiple applications of creating animation, etc.

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
#Description:
#For a two-dimensional array, in order to reference every element, we must use two nested loops.
#This gives us a counter variable for every column and every row in the matrix. int cols = 10; int rows = 10; int [] [] myArray = new int [cols] [rows];
# Two nested loops allow us to visit every spot in a 2D array Creating Arrays.
#You can create an array by using the new operator with the following syntax − Syntax arrayRefVar = new dataType[arraySize]; 
#The above statement does two things − It creates an array using new dataType[arraySize]. 
#It assigns the reference of the newly created array to the variable arrayRefVar.


import numpy
from PIL import Image
imarray = numpy.random.rand(512,512,3) * 255
imarray[0:512,0:512] = [100,0,255]
im = Image.fromarray(imarray,'RGB')
im.save('Generated_Image.jpg')
im.show()

# Assignment:	
   # 1. Develop a program to find the neighbours of each element in the matrix
   # Description:
   #In topology and related areas of mathematics, a neighbourhood (or neighborhood) is one of the basic concepts in a topological space.
   It is closely related to the concepts of open set and interior.
   #Intuitively speaking, 
   #a neighbourhood of a point is a set of points containing that point where one can move some amount in any direction away from that point without leaving the set. 


   
 ## Develop a program to find the neighbours of each element in the matrix.
 ## Write a program to find the sum of neighbour values in a matrix.

    import numpy as np
axis = int(input("Enter the radius of the matrix: "))
neighbor = int(input("Enter the 4 or 8 to calculate the neighbors: "))
if neighbor == 4 or neighbor == 8:
    x =np.empty((axis,axis))
    y = np.empty((axis+2,axis+2))
    s =np.empty((axis,axis))
    
    # Generating the Values of the Matrix
    for i in range(0,axis):
        for j in range(0,axis):
            x[i][j]=int(i+j+1)
    # Printing the Values of the Generated Matrix
    print("Printing the Values of the Generated Matrix", end="\n")
    for i in range(0,axis):
        for j in range(0,axis):
            pass
            print(int(x[i][j]),end = '\t')
        print('\n')


    for i in range(0,axis+2):
        for j in range(0,axis+2):
            if i == 0 or i == axis+1 or j == 0 or j==axis+1:
                y[i][j]=0
            else:
                y[i][j]=x[i-1][j-1]
                
    # Printing the Values of the Matrix after padding with zeros
    print("The Values of the Matrix after padding with zeros:", end="\n")
    for i in range(0,axis+2):
        for j in range(0,axis+2):
            print(int(y[i][j]),end = '\t')
        print('\n')
    
    print("The neighbours of each element in the matrix:", end="\n")
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
        
    print("The following matrix contains the sum of neighbour values in a matrix")
    for i in range(0,axis):
        for j in range(0,axis):
            
            if neighbor == 4:                
                s[i][j]=((y[i][j+1]+y[i+1][j]+y[i+1][j+2]+y[i+2][j+1]))
                print(s[i][j],end = '\t')
            elif neighbor ==8:
                s[i][j]=((y[i][j]+y[i][j+1]+y[i][j+2]+y[i+1][j]+y[i+1][j+2]+y[i+2][j]+y[i+2][j+1]+y[i+2][j+2]))
                print(s[i][j],end = '\t')
        print('\n')
else:
     print("Wrong neighbors, you have to select ether 4 or 8")
 

## Write a C++ program to perform operator overloading.

#include "bits/stdc++.h" 
#include <vector>
#define rows 5
#define cols 5 
using namespace std; 
int N; 

class Matrix { 
	int arr[rows][cols]; 
public: 
	void input(vector<vector<int> >& A); 
	//void display() ; 
	void operator=(Matrix x);
	void operator+(Matrix x); 
	void operator-(Matrix x); 
	void operator*(Matrix x);
	
}; 

void Matrix::input(vector<vector<int> >& A) 
{ 
	for (int i = 0; i < rows; i++) { 

		for (int j = 0; j < cols; j++) { 

			arr[i][j] = A[i][j]; 
		} 
	}
 
} 

void Matrix::operator=(Matrix x) 
{ 
	// Travarse the Matrix x 
	for (int i = 0; i < rows; i++) { 
		for (int j = 0; j < cols; j++) { 
			arr[i][j] =  x.arr[i][j]; 
		} 
	}
	
	for (int i = 0; i < rows; i++) { 

		for (int j = 0; j < cols; j++) { 

			// Print the element 
			cout << arr[i][j] << ' '; 
		} 
		cout << endl; 
	} 
	cout <<"#######################"<< endl; 

} 

void Matrix::operator+(Matrix x) 
{ 

	int mat [rows][cols]; 
	for (int i = 0; i < rows; i++) { 
		for (int j = 0; j < cols; j++) { 
			mat[i][j] = arr[i][j]+ x.arr[i][j]; 
		} 
	} 
   for (int i = 0; i < rows; i++) { 

		for (int j = 0; j < cols; j++) { 
			cout << mat[i][j] <<"\t"; 
		} 
		cout << endl; 
	} 
	cout <<"#######################"<< endl; 
} 


void Matrix::operator-(Matrix x) 
{ 

	int mat[rows][cols]; 


	for (int i = 0; i < rows; i++) { 

		for (int j = 0; j < cols; j++) { 
			mat[i][j] = arr[i][j] 
						- x.arr[i][j]; 
		} 
	} 
for (int i = 0; i < rows; i++) { 

		for (int j = 0; j < cols; j++) { 

			cout << mat[i][j] << ' '; 
		} 
		cout << endl; 
	} 
	cout <<"#######################"<< endl; 

} 


void Matrix::operator*(Matrix x) 
{ 

	int mat[rows][cols]; 
	for (int i = 0; i < rows; i++) { 

		for (int j = 0; j < cols; j++) { 
			mat[i][j] = 0; 

			for (int k = 0; k < rows; k++) { 
				mat[i][j] += arr[i][k] 
							* (x.arr[k][j]); 
			} 
		} 
	} 

for (int i = 0; i < rows; i++) { 

		for (int j = 0; j < cols; j++) { 

			cout << mat[i][j] <<"\t"; 
		} 
		cout << endl; 
	} 
	cout <<"#######################"<< endl; 

} 

int main() 
{ 

vector<vector<int> > v1 (rows, vector<int> (cols, 0));
vector<vector<int> > v2(rows, vector<int> (cols, 0)) ;
	
		for (int i = 0; i < v1.size(); i++) { 
		
		for (int j = 0; j < v1[i].size(); j++) { 
			v1[i][j] = i+j+1; 
			cout<<v1[i][j]<<" ";
		} 
		cout<<endl;

	} 
	
	Matrix m1, m2; 
	m1.input(v1); 
	cout << "intializing Second Matrix using assignment Operator"<<endl;
	m2 = m1;
	cout << "Addition of two given"
		<< " Matrices is : \n"; 
	m1 + m2; 

	cout << "Substraction of two given"
		<< " Matrices is : \n"; 
	m1 - m2; 

	cout << "Multiplication of two"
		<< " given Matrices is : \n"; 
	m1* m2; 

	return 0; 
}

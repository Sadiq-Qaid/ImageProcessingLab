# 1: Program output to display grayscale image using read and write operations

# 1.a.	Scaling output:

![image](https://user-images.githubusercontent.com/72355871/104435128-074da200-55b2-11eb-8427-719c07172747.png)

# 1.b. Rotation output:
# Description
In digital photography, computer-generated imagery, and colorimetry, a grayscale or image is one in which the value of each pixel is a single sample representing only an amount of light; that is, it carries only intensity information. Grayscale images, a kind of black-and-white or gray monochrome, are composed exclusively of shades of gray.

To convert an image to grayscale in any of the Microsoft Office suite apps, right-click it and select Format Picture from the context menu . This will open an image editing panel on the right. Go to the Picture tab (the very last one). Expand the Picture Color options, and click the little dropdown next to the Presets for Color Saturation.
# code
import cv2
img= cv2.imread("app.jpg")

gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imwrite("opencv-greyscale.png",gray_image)

cv2.imshow("Orignal",img)

cv2.imshow("Gray_Scale",gray_image)

cv2.waitKey(0)

cv2.destroyAllWindows()

# Output

![image](https://user-images.githubusercontent.com/72355871/104437078-5eed0d00-55b4-11eb-96e6-3bd6163982fa.png)

# 2: Program Output to find sum and mean of a set of images
# Output:
![image](https://user-images.githubusercontent.com/72355871/104437323-a1aee500-55b4-11eb-89c6-e58f10bba8a1.png)


# 3: Program Output for to convert image into a binary (Black and white) colour

![image](https://user-images.githubusercontent.com/72355871/104437487-d15ded00-55b4-11eb-8129-0d7315628bec.png)


# 5: Program Output to convert the given colour image to different colour spaces.

![image](https://user-images.githubusercontent.com/72355871/104437594-fd796e00-55b4-11eb-9986-27bcff1ee3c7.png)

# 6: Program Output to create an image from 2D array (create an array of random size and density values).

![image](https://user-images.githubusercontent.com/72355871/104437683-1e41c380-55b5-11eb-8b14-d6fbc3fac39e.png)

![image](https://user-images.githubusercontent.com/72355871/104442904-be025000-55bb-11eb-8d1b-0914506c2e38.png)

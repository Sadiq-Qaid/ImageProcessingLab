Develop a program to display grayscale image using read and write operations
import cv2
img= cv2.imread("app.jpg")
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("opencv-greyscale.png",gray_image)
cv2.imshow("Orignal",img)
cv2.imshow("Gray_Scale",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

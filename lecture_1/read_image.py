import cv2

img1 = cv2.imread('D:\\computer vision bootcamp\\image_1.jpg')
cv2.imshow('THe original Image', img1)
cv2.waitKey(0)


cv2.imwrite('saced_original_image.jpg', img1)
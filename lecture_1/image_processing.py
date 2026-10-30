import cv2
img = cv2.imread('lena.jpg')


# reszing
resizing  = cv2.resize(img, (640, 480))

# gray
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blurring
blurring = cv2.GaussianBlur(img, (5,5), 0) # img, kernel, 0-> std devisation 0 means automatic

# edges
edges = cv2.Canny(img, 100, 200)

# cv2.imshow('Resized Image', resizing)
# cv2.imshow('Grey Image', grey)
# cv2.imshow('Blurring Image', blurring)
cv2.imshow('Edges Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
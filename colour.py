import cv2


# Xml file from OpenCv to detect the face
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


# Read the image
img = cv2.imread("Images/sign.png")
img = cv2.resize(img, (400,400))


# Convert the image into a gray colour format (black&white)
g_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


# Detect the most frequent colour in a image
b,g,r = (img[300, 300])
print (r)
print (g)
print (b)


cv2.imshow("main", img)



cv2.waitKey()
cv2.destroyAllWindows()
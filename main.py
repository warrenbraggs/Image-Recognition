import cv2


# Xml file from OpenCv to detect the face
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


# Read the image
img = cv2.imread("people1.jpg")
img = cv2.resize(img, (400,400))


# Convert the image into a gray colour format (black&white)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Search the co-ordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors=3)


for x,y,w,h in faces:
	img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),3)


cv2.imshow("main", img)



cv2.waitKey()
cv2.destroyAllWindows()
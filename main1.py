import cv2


# Xml file from OpenCv to detect the face
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Start video capture 	(0) -> from webcam
#						('input_your_filename') -> from a file			
cap = cv2.VideoCapture(0)



while True:
	_, img = cap.read()

	# Convert the image into a gray colour format (black&white)
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Search the co-ordinates of the image
	faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors=3)

	# Draw a rectangle if a face is found
	for x,y,w,h in faces:
		img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),3)


	cv2.imshow("main", img)

	# Use the command ESC to exit
	if cv2.waitKey(1) == 27 and 0xFF:
		break

cap.release()
cv2.destroyAllWindows()
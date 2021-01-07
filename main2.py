#Text recognition

import cv2
import pytesseract 

#Add the path for tesseract
pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/4.1.1/bin/tesseract"

#Read the image
img = cv2.imread("Images/alpha2.png")

#Convert the image
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Print the characters detect in the terminal
print(pytesseract.image_to_string(img, lang='eng',config='--psm 6'))


# Get the size of the image
h_image = img.shape[0]
w_image = img.shape[1]

# Detect the characters in the image
boxes = pytesseract.image_to_boxes(img, lang='eng',config='--psm 6')

for i in boxes.splitlines():
    i = i.split(' ')
    x,y,w,h = int(i[1]), int(i[2]), int(i[3]), int(i[4])
    cv2.rectangle(img, (x, h_image-y), (w,h_image-h), (0,255,0),2)


#Display the image
cv2.imshow('main', img)
cv2.waitKey(0)
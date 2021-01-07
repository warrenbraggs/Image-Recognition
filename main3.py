#Text recognition real time

import cv2
import pytesseract 
from PIL import Image 


#Add the path for tesseract
pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/4.1.1/bin/tesseract"


#Start video capture    (0) -> from webcam
#                       ('input_your_filename') -> from a file          
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()

    #Convert the image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Print the characters detected in the terminal
    print(pytesseract.image_to_string(Image.fromarray(img)))

    # Get the size of the frame
    h_image = img.shape[0]
    w_image = img.shape[1]

    # Detect the characters in the frame
    boxes = pytesseract.image_to_boxes(Image.fromarray(img))

    for i in boxes.splitlines():
        i = i.split(' ')
        x,y,w,h = int(i[1]), int(i[2]), int(i[3]), int(i[4])
        cv2.rectangle(img, (x, h_image-y), (w,h_image-h), (0,255,0),2)
    

    #Display the frame
    cv2.imshow('main', img)

    # Use the command ESC to exit
    if cv2.waitKey(1) == 27 and 0xFF:
        break

cap.release()
cv2.destroyAllWindows()

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

    # Convert the image
    # BGR2BGRA = Real colours
    # BGR2HSV = For colour detection
    #t_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Detect the most frequent colour in a image
    b,g,r = (img[300, 300])
    print (r)
    print (g)
    print (b)


    # Print the characters detected in the terminal
    print(pytesseract.image_to_string(Image.fromarray(img)))

    #
    #
    #
    #
    #

    
    #Display the frame
    cv2.imshow('main', img)

    # Use the command ESC to exit
    if cv2.waitKey(1) == 27 and 0xFF:
        break

cap.release()
cv2.destroyAllWindows()

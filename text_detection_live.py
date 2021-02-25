#Text recognition real time

import cv2
import numpy as np 
import pytesseract 
from PIL import Image 



#Add the path for tesseract
pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/4.1.1/bin/tesseract"


#Start video capture    (0) -> from webcam
#                       ('input_your_filename') -> from a file        

count = 0

cap = cv2.VideoCapture(0)

while cap.isOpened():
    count +=1

    if count%20 == 0:
        _,img = cap.read()

        # Convert the image
        # BGR2BGRA = Real colours
        # BGR2HSV = For colour detection
        #t_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


        # setting values for base colors 
        b = img[:, :, :1] 
        g = img[:, :, 1:2] 
        r = img[:, :, 2:] 
      
        # computing the mean 
        b_mean = np.mean(b) 
        g_mean = np.mean(g) 
        r_mean = np.mean(r) 
      
        # displaying the most prominent color 
        print(r_mean)
        print(g_mean)
        print(b_mean)


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

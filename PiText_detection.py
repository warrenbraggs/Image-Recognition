import cv2 
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

rawCapture = PiRGBArray(camera, size=(640, 480))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    
    rawCapture.truncate(0)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    text = pytesseract.image_to_string(img, config='')
    print(text)
    
    # Detect the most frequent colour in a image
    b,g,r = (img[300, 300])
    print (r)
    print (g)
    print (b)

    

    if key == ord("s"):
        cv2.waitKey(0)
        break

cv2.destroyAllWindows()

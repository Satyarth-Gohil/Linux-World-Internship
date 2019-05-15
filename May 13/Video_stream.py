
import cv2
cap=cv2.VideoCapture(0)


while True:
    ret,photo=cap.read()
    cv2.imshow('hi',photo)
    if cv2.waitKey(1)==13: # here 13 is the value of 'Enter' key in waitkey function
        break    
cv2.destroyAllWindows()
cap.release()


import cv2

cap=cv2.VideoCapture(0)
ret,photo=cap.read()
cv2.imwrite('/root/Desktop/pendrive.png',photo)
cap.release()

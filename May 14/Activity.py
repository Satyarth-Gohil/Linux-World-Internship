import os
import subprocess as sp
import pyttsx3
import cv2
import numpy as np

os.system("tput setaf 1")
print("\t\t\tWelcome to my menu.")
os.system("tput setaf 0")
print("\t\t\t-------------------")

print(""" 
press 1 : to convert your image in red
press 2 : to convert your image in green
press 3 : to convert your image in Blue
press 4 : to convert your image in Graysacle
press 5 : to exit
""")

speaker=pyttsx3.init()
speaker.say("Enter your Choice")
speaker.runAndWait()

print("Enter your choice: ",end = " ")
ch=input()
print(ch)
a1=np.zeros([480,640],dtype="uint8")
x=cv2.VideoCapture(0)
ret,image=x.read()
x.release()
if int(ch)==1:
	B,G,R=cv2.split(image)
	R_image=cv2.merge([a1,a1,R])
	cv2.imshow('image',R_image)
	cv2.waitKey()
	cv2.destroyAllWindows()
	print(x)
elif int(ch)==2:
	B,G,R=cv2.split(image)
	G_image=cv2.merge([a1,G,a1])
	cv2.imshow('image',G_image)
	cv2.waitKey()
	cv2.destroyAllWindows()
elif int(ch)==3:
	B,G,R=cv2.split(image)
	B_image=cv2.merge([B,a1,a1])
	cv2.imshow('image',B_image)
	cv2.waitKey()
	cv2.destroyAllWindows()
elif int(ch)==4:
	BW_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	cv2.imshow('image',BW_image)
	cv2.waitKey()
	cv2.destroyAllWindows()
elif int(ch)==5:
	print("exit")


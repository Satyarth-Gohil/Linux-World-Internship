import os
import subprocess as sp
import pyttsx3
import cv2

os.system("tput setaf 1")
print("\t\t\tWelcome to my menu.")
os.system("tput setaf 0")
print("\t\t\t-------------------")

print(""" 
press 1 : to check date
press 2 : to open cal
press 3 : to create user
press 4 : to create file
press 5 : to capture video
press 6 : to exit
""")

speaker=pyttsx3.init()
speaker.say("Enter your Choice")
speaker.runAndWait()

print("Enter your choice: ",end = " ")
ch=input()
print(ch)

if int(ch)==1:
	x=sp.getoutput("date")
	print(x)
elif int(ch)==2:
	x=sp.getoutput("cal")
	print(x)
elif int(ch)==3:
	print("Enter the User name:",end=" ")
	user_name=input()
	sp.getoutput("adduser {}".format(user_name))
elif int(ch)==4:
	print("Enter Your Filename:",end=" ")
	file_name=input()
	x=sp.getoutput("touch {}".format(file_name))
elif int(ch)==5:
	cap=cv2.VideoCapture(0)
	while True:
	    ret,photo = cap.read()
	    cv2.imshow('hi',photo)
	    if cv2.waitKey(1)==13 :
	        break ;
	cv2.destroyAllWindows()
	cap.release()
elif int(ch)==6:
	print("exit")

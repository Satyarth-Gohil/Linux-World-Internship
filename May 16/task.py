import os
import subprocess as sp
import pyttsx3
import cv2
speaker=pyttsx3.init()

os.system("tput setaf 1")
print("\t\t\tWelcome to my menu.")
speaker.say("Welcome to my menu.")
speaker.runAndWait()
os.system("tput setaf 0")
print("\t\t\t-------------------")

print(""" 
press 1 : to check date
press 2 : to open cal
press 3 : to create user
press 4 : to create file
press 5 : to capture video on the front door
press 6 : to exit
""")

speaker.say("""press 1 : to check date
press 2 : to open cal
press 3 : to create user
press 4 : to create file
press 5 : to capture video on the front door
press 6 : to exit""")
speaker.runAndWait()

speaker=pyttsx3.init()
speaker.say("Enter your Choice")
speaker.runAndWait()

print("Enter your choice: ",end = " ")
ch=input()
print(ch)

if int(ch)==1:
	x=sp.getoutput("date")
	print(x)
	speaker.say(x)
	speaker.runAndWait()
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
	face_model=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
	cap=cv2.VideoCapture(0)
	while True:
    		ret,photo=cap.read()
    		coord=face_model.detectMultiScale(photo)
    		if len(coord)>=1:
    			j=len(coord)
    			speaker.say("There are {} people on the front door".format(j))
    			speaker.runAndWait()
    			for i in range(len(coord)):
        			x1=coord[i][0]
        			y1=coord[i][1]
        			x2=coord[i][0]+coord[i][2]
        			y2=coord[i][1]+coord[i][3]
        			cv2.rectangle(photo,(x1,y1),(x2,y2),(255,255,0),2)
    		cv2.imshow('hi',photo)
    		if cv2.waitKey(1)==13:
        		break
	cv2.destroyAllWindows()
	cap.release()
elif int(ch)==6:
	print("exit")

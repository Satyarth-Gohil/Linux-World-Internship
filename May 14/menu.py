import os
import subprocess as sp
import pyttsx3

os.system("tput setaf 1")
print("\t\t\tWelcome to my menu.")
os.system("tput setaf 0")
print("\t\t\t-------------------")

print("Where you want to run this tools (local/remote): ",end=" ")
location=input()

print(""" 
press 1 : to check date
press 2 : to open cal
press 3 : to create user
press 4 : to create file
press 5 : to exit
""")
print(location)
speaker=pyttsx3.init()
speaker.say("Enter your Choice")
speaker.runAndWait()

print("Enter your choice: ",end="")
ch=input()

if location=="local" :
	if int(ch)==1:
		os.system("date")
	elif int(ch)==2:
		x=sp.getoutput("cal")
		print(x)
	elif int(ch)==3:
		print("User")
	elif int(ch)==4:
		print("Enter Your Filename:",end=" ")
		file_name=input()
		x=sp.getoutput("touch {}".format(file_name))
	elif int(ch)==5:
		print("exit")
elif location=="remote":
	print("Enter remote IP: ",end=" ")
	ip=input()
	if int(ch)==1:
		x=sp.getoutput("ssh {} date".format(ip))
		print(x)
	elif int(ch)==2:
		x=sp.getoutput("ssh {} cal".format(ip))
		print(x)
	elif int(ch)==3:
		print("Enter the user name: ",end=" ")
		user_name=input()
		x=sp.getoutput("ssh {} useradd {}".format(ip,user_name))
		print(x)
	elif int(ch)==4:
		print("Enter the file name: ",end=" ")
		file_name=input()
		x=sp.getoutput("ssh {} touch {}".format(ip,file_name))
		print(x)
	elif int(ch)==5:
		print("exit")

# Operating System (OS) - Red Hat Enterprise Linux (RHEL) - Version 7.5, 8

OS - Multiple programs creating an environment.

Memory Unit : RAM (Volatile)
Storage Unit : Hard Disk (Persistent)
Compute Unit : CPU + RAM

Bare Metal : DOS

Two ways of interaction with a computer:
CLI - Command Line Interface (Using only commands and syntax.)
GUI - Graphical User Interface (Using images, animations, graphs, etc.)

# Linux Commands

	- which firefox # gives where the given program is located on the os
	- gedit /usr/bin/firefox # opens the code of the given file in an editor. Here the path of firefox is given, so it will open firefox's code.

#Miscellaneous:
Password Request --> Server --send--> Tokens (cookies) ---save-locally--> HDD
--> If cookies are exposed data breaches can take place

Technically anything in OS can be accessed via a file or a folder.
To access a device in computer we need its drivers to be installed.
Softwares are ditributed in the forms of the packages, when they are to be installed these packages are used.
In windows packages are in the form of .exe files and in Red Hat packages are in the form of .rpm files.

# Linux Commands

	- rpm -q -f /usr/bin/date # q-> query f-> file, this command gives details of the files which are queried about.
	- rpm -e firefox # e -> erase. This commannd erases the files of the program firefox.
	- rpm -i firefox # i -> install. This command installs the given program files, here firefox.
	- rpm -q vlc # This command queries for program VLC and if it is installed it will display its versions.
	- yum whatprovides firefox # this command will show which file is required to download or install the given program.
	- yum install firefox # this command installs firefox software.
	- rpm -q python36
	- man date # this command is used to give the mannual for using that software or program or any command.
--> Use Ctrl+C to close any program.
--> If Ctrl+Z is used to close the program, then the program closes but it keeps running in the background and consumes the memory.
	- jobs # this command lists all the jobs running in the background.
--> All the jobs that are closed using Ctrl+Z are paused and kept in the background - jobs command lists those background programs.
	- fg[1] # this command opens program with id [1] in foreground from the background.
	- firefox & # this command keeps the program running as well as opens up a new prompt on the terminal window.
--> TTS - Text To Speech
	- echo hello | festival --tts # In this command the output of 'echo hello' is sent to the 'festival tts' command via pipe (|) symbol.
	- echo 'apple pie' | festival --tts # apple pie is spoke in the speaker via text to speech command.
--> We use Ctrl+D to exit live interpreter like python on CLI mode.

# Python

--> REPL - Read Evaluate Print Loop
- type(x) # gives the data type of x variable
--> Type i/nference - Python automatically infers the datatype of the variable.
--> Data Type : List
--> (:) colon symbol is used as the slicing operator in the lists.
	- x[:3] <=> x[0:3]
	- x[1:] <=> x[1:n]
	- x[:] <=> x[0:n] <=> x
--> lists can be of multiple dimensions

eg:
	- l=[1,2,3,4] # 1 dimension list
	- l=[[x,y],[a,b],[c,d]] # 2 dimension list
	- l=[[[1,2],[3,4]],[[5,6],[7,8]]] # 3 dimension list
--> this way lists on n multiple dimensions can be built.

--> List Data type doesn't support column wise operations, they support only row wise or element to element operations.
--> We use 'Numpy' Arrays to perform  columnwise  operations.
- system(gnome-terminal) #this command is used to run linux terminal commands on python.
--
	- import os # imports OS module which is needed to run the system command.
	- os.system(date) # this command runs date command of linux in the python code.
--> We would require pip3.6 software to install any module in python.
	- yum whatprovides pip3.6
	- yum install pip3.6
--> To install any module in python we use  --pip3.6 install module_name-- command. This command installs the module using pip3.6 software.
-->For coding in python we will also use an IDE (Integrated Development Environment) software named Jupyter Notebook.
	- pip3.6 install jupyternotebook...
	- jupyter notebook --allow-root
--> We will use cv2 module to do image-processing in python
	- pip3.6 install cv2

****read 11_May.ipynb to get information about Numpy and Image-Processing Using CV2 in Python****

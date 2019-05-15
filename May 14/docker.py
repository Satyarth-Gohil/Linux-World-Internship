# This program runs 10 container os on the docker
import subprocess as sp
i=0
while i<10:
	sp.getoutput("docker run -dit ubuntu:14.04")
	i=i+1


#!/usr/bin/python
import time, sys, subprocess, os, re

os.system("printf \"\\033c\"")
#clear console, fresh start

#prints input char by char
def printCbyC(input, wait):
  for c in input:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(wait)
open("output.txt", "w+")

#phihags suggestion, modified slightly for handiness
subprocess.check_output("for card in /sys/class/drm/card*/* ; do echo \"$card: $(head -n 1 $card/modes)\">>output.txt; done", shell=True)

os.system("clear")

with open("output.txt") as f:
    content = f.readlines()
#find the resolutions (every odd will be the width, every even the height i.e. [1920,1080,800,600])
resolution = []
for piece in content:
	
	temp = re.search("([0-9]{2,})[Xx]([0-9]{2,})", piece)
	if temp:
		resolution.append(int(temp.group(1)))
		resolution.append(int(temp.group(2)))

os.system("/bin/setfont /usr/share/consolefonts/Uni3-Terminus14.psf.gz")
width = resolution[0]/8
height = resolution[1]/14
for i in range(0,height-1):
	if i == 0 or i == height-2:
		for j in range(0,width):
			os.system("tput cup " + str(i) + " " + str(j))
			printCbyC("#",0)
	os.system("tput cup " + str(i) + " " + str(0))
	printCbyC("#",0)
	os.system("tput cup " + str(i) + " " + str(width))
	printCbyC("#",0)


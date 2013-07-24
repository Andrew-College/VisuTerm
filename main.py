#!/usr/bin/python
import time, sys, subprocess, os, re

os.system("printf \"\\033c\"")
#clear console, fresh start

#prints input
def printCh(input):
  for c in input:
    sys.stdout.write(c)
    sys.stdout.flush()
    
#prints input char by char
def printCbyC(input, wait):
  for c in input:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(wait)

#generates icons and coords
def icons(screenRes):
	whatsHere = str(os.system("ls"))
	if(whatsHere[-1] == "0"):
		#remove 0
		whatsHere = whatsHere[:-2].rstrip()
	else:
		print "Error in ls output; " + whatsHere[-1]
	
	print whatsHere
	
	

#paints everything on to the screen
def screenpaint(screenRes):
	os.system("clear")
	width = screenRes[0]/8
	height = screenRes[1]/14
	for i in range(0,height-1):
		if i == 0 or i == height-2:
			for j in range(0,width):
				os.system("tput cup " + str(i) + " " + str(j))
				printCh("#")
		os.system("tput cup " + str(i) + " " + str(0))
		printCh("#")
		os.system("tput cup " + str(i) + " " + str(width))
		printCh("#")
	icons(screenRes)

#Lets get main-gerous
def main():
	#phihag(of StackOverflow fame)s suggestion, modified slightly for handiness
	subprocess.check_output("for card in /sys/class/drm/card*/* ; do echo \"$card: $(head -n 1 $card/modes)\">>output.txt; done", shell=True)
	
	os.system("clear")
	
	with open("output.txt") as f:
	    content = f.readlines()
	#find the resolutions (every odd will be the width, every even the height i.e. [1920,1080,800,600])
	resolution = []
	for value in content:
		#Is it in the form -num(2 or more),x,num(2 or more)- i.e. 800x600 
		#Won't work on miniscule screens ((9x9 resolution XD))
		#note to future coder person, is it really necessary to use a res so small?
		#The 'icons' will look messy/ might fail
		temp = re.search("([0-9]{2,})[Xx]([0-9]{2,})", value)
		if temp:
			resolution.append(int(temp.group(1)))
			resolution.append(int(temp.group(2)))
	
	os.system("/bin/setfont /usr/share/consolefonts/Uni3-Terminus14.psf.gz")
	screenpaint(resolution)
	
main()

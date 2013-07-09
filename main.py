#!/usr/bin/python
import time, sys, subprocess, os, re
#os.system("xrandr  | grep \* | cut -d' ' -f4 >resolution.txt")outdated, using subprocess

os.system("printf \"\\033c\"")
#clear console, fresh start

#prints input char by char
def printCbyC(input, wait):
  for c in input:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(wait)
open("output.txt", "w+")
#printCbyC("something", .3)

subprocess.check_output("for card in /sys/class/drm/card*/* ; do echo \"$card: $(head -n 1 $card/modes)\">>output.txt; done", shell=True)
os.system("clear")
with open("output.txt") as f:
    content = f.readlines()
#find the resolutions (every odd will be the width, every even the height i.e. [1920,1080,800,600])
resolution = []
for piece in content:
	temp = re.search("([0-9]{2,})[Xx]([0-9]{2,})", piece)
	if temp:
		resolution.append(temp.group(1))
		resolution.append(temp.group(2))
	


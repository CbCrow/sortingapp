# Collin Crowthers 10/4/21
# Sort names by length and alphabetical order
# Input is a file named Sort Me.txt and must be located in the same directory as this file

import os
import argparse

#set up the path the file is located in. not sure how to do this with stdin so I used os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

parser = argparse.ArgumentParser()
parser.add_argument('-r', action='store_true')
args = parser.parse_args()

rtrue = args.r


#make the list to hold the names
lines = []

#putting the names from the file into the list
for line in open(os.path.join(__location__, 'Sort Me.txt')):
    lines.append(line.strip())

#removes the extra space at the start of the file
if (lines[0] == ''):
    del lines[0]

#this does an alphabetical sort
lines.sort()

#this sorts by length, and according to documentation is a stable sort. this means that
#lines of the same length will keep their previous order (alphabetical), but if they differ
#then the length will be sorted
lines = sorted(lines, key=len)

#print the list
if(rtrue == True):
    for x in reversed(lines):
        print(x)
else:
    for x in lines:
        print(x)
#!/usr/bin/env python3
	
import re

#python 7 problem 6, regular expression to find and print all occurences of R and Y
raw = open("Python_07_ApoI.fasta", "r") 
for line in raw:
	found = re.findall(r"\wAATT\w", line) #seqn is RAATTY where R and Y are divergent
	#print(found)

#problem 7, print the occurences above as places of cleavage on the seqn. denote as R^AATTY
	replacement = re.sub(r"\wAATT\w", "R^AATTY", line)
	print(replacement)
	products = re.findall(r"R^AATTY", line)

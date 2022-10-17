#!/usr/bin/env python3

import re

#Python 7 exercises 

#replacement and count of words in a txt file with output 
Somebody = {}

with open("Python_07_nobody.txt", "r") as raw, open("nobody_someone.txt","w") as irewrite:
	for line in raw:
		line = line.rstrip()
		for match in re.finditer(r'Nobody', line):
			pos_start = match.start() + 1
			pos_end = match.end()
#		print(pos_start, pos_end)
		line = re.sub('Nobody', 'Somebody', line)
		line = line.split("\n")
#		rewrite.write(line)

#using matching to find all header lines
fa_header = {}
with open("Python_07.fasta", "r") as fasta7:
	for line in fasta7:
		line = line.rstrip()
#		for match in re.finditer(r'>...\d{1,6}.\w{2,6}.\w\d{1,6}.\d..{1,99}', line):
#			print(match)
#		for gene in re.finditer(r'>...\d{1,6}.\w{2,6}.\w\d{1,6}.\d.', line):
#			print(gene)
		for description in re.finditer(r'/s.{1,99}', line):
			print(description)
				
#previous fasta parser developed in python 6_2 problem set, moedified to use regular expression
fasta_parser = {}
with open("Python_07.fasta","r") as raw_fasta, open("fasta_parser.fasta", "w") as fast_parc:
	for line in raw_fasta:
		line = line.rstrip()
		gene = re.findall(r'>...\d{1,6}.\w{2,6}.\w\d{1,6}.\d..{1,99}', line) 
		if gene == line: 
			gene = line.lstrip(">")
		else:
			seqn = line
			print(gene)
			fasta_parser[gene] = seqn 
for k, v in fasta_parser.items():
  print(k,v)
				
			 

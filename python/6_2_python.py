#!/usr/bin/env python3

#second half of python 6 excercises
lines = {}
characters = {}
length = {}
#with open("Python_06.fastq", "r") as raw, open("Python_06.fasta","w") as fastq_write: 
#	for line in raw:
#			lines = 
#			characters = 
#			length = len(line)
#		fastq_write.write(lines + characters + length)

#fasta parser
fasta_p = {}
with open("Python_06.fasta","r") as raw_fasta, open("fasta_parser.fasta", "w") as fast_parc:
	for line in raw_fasta:
		line = line.rstrip()
		if line.startswith(">"):
			gene = line.lstrip(">")
		else:
			seqn = line
			fasta_p[gene] = seqn 
for k, v in fasta_p.items():
	print(k,v)

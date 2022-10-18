#!/usr/bin.env python3

fasta_ecoli = {}
#NGS workshop problem set 
fasta = open("Ecoli.fasta", "r")
for line in fasta:
	line = line.rstrip()
	if line.startswith(">"):
		gene = line.lstrip()
#		print(gene)
	else:
#		print(len(line)) #prints line lengths but not the total lengths in the fasta
		seqn = line
		fasta_ecoli[gene] = seqn #dictionary is built 
#print(fasta_ecoli.items()) #prints dictionary key; values
#print(len(seqn))	#prints 1? 
#print(fasta_ecoli.values()) #prints only a few bases for each gene?





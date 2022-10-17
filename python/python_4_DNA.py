#!/usr/bin/env python3

DNA_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for DNA in DNA_list:
	print(DNA)
	print(len(DNA))  

DNA_list_lengths = [(len(DNA),DNA) for DNA in DNA_list]
print(DNA_list_lengths)

DNA_pos_len = ([

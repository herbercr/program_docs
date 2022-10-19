#!/usr/bin/env python3

#script to automate xcalibur quantification output
##NEED TO HAVE ANACONDA, PANDAS, AND XLRD INSTALLED FOR THIS SCRIPT TO RUN##

import pandas as pd
import xlrd as xl
import sys
testxls = open("test.txt","w") 

xls = pd.read_excel("8oa8og_Sean_Final_Long.XLS", sheet_name=None, header=0, index_col=0, usecols="A,O", skiprows=4)
#print(xls) #use to check if calling the correct data
mods = xls.keys() 
#print(f'Modifications:, {str(mods)}) #prints the names of the modifications in the export xls
xls_pd = pd.DataFrame(xls)

xls.rename(columns = {O:sheet_name}, inplace=True) 
mods = {}
mods = {}



###for printing stdout to a file
#from contextlib import redirect_stdout

#with open('out.txt', 'w') as f:
#	with redirect_stdout(f):
#		print('data')



###for writing stdout to an output file
#orig_stdout = sys.stdout
#f = open('out.txt', 'w')
#sys.stdout = f

#for i in range(2):
#	print('i = ', i)

#sys.stdout = orig_stdout
#f.close()

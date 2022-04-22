# Author: Dr. Muniba Faiza
# Copyright Muniba Faiza 2022


#!/usr/bin/env python3

import os
import os.path
import pathlib
import glob
import itertools
import collections
import pprint
import sys
import re


# Path to DSSP files
input_path = os.getcwd()+"/dssp_files"


# Read all filenames in the dir
file_list = os.listdir(input_path)

# Path to output direcotry
output_path = os.getcwd()+"/longH_output"


#collecting the total number of dssp files in the directory.
num_files = len(glob.glob1(input_path,"*.dssp"))
print('There are',num_files, 'dssp files in the input directory\n\n')


#looking for long helices
matches = ["H  >", "H  <", "H  3>", "H  3<", "H  4", "H  X", "H >", "H 3", "H <", "H X", "H 4"]


for file_name in file_list:

	import fnmatch

	if fnmatch.fnmatch(file_name, '*.dssp'):
		
		with open(os.path.join(input_path, file_name), "r") as src_file:


			line_was_helix = 0
			filecounter = 0
			line_is_helix = 0

			last_line_matched = 0

			# long helix
			for line in src_file:
					
					set_line_header = ''
					if '#' in line:
						line_header = line
						set_line_header = line_header
					last_line_matched = line_is_helix
					line_is_helix = 0

					for helix in matches:						
						if helix in line:
							line_is_helix = 1

					if line_is_helix ==1:
					
						if not last_line_matched:
							filecounter +=1
							set_line_header = line_header

						#change to output directory						
						os.chdir(output_path)
						
						#create an output file and append helix to it.
						with open(file_name+"_H_"+str(filecounter)+".dssp", "a") as h:
							print(set_line_header+"\n"+line+"\n",file=h)
							h.close()
	else:
		continue
print("The output is provided in longH_output directory.")

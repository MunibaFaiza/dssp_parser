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


input_path = os.getcwd()+"/dssp_files"


#read all filenames in the dir

file_list = os.listdir(input_path)
#print(file_list)

output_path = os.getcwd()+"/shortH_output"


#collecting the total number of log files in the directory.

num_files = len(glob.glob1(input_path,"*.dssp"))
print('There are',num_files, 'dssp files in the current directory\n\n')


short_matches = ["G 3", "G 4", "G X","G >", "G <", "G  3", "G  X","G  >", "G  <", "G  4"]



for file_name in file_list:

	import fnmatch

	if fnmatch.fnmatch(file_name, '*.dssp'):
		with open(os.path.join(input_path, file_name), "r") as src_file:




			line_was_helix = 0
			filecounter = 0
			line_is_helix = 0

			last_line_matched = 0

			# short helix
			for line in src_file:
					
					set_line_header = ''
					if '#' in line:
						line_header = line
						set_line_header = line_header
					last_line_matched = line_is_helix
					line_is_helix = 0

					for helix in short_matches:						
						if helix in line:
							line_is_helix = 1

					if line_is_helix ==1:
					
						if not last_line_matched:
							filecounter +=1
							set_line_header = line_header

						
						os.chdir(output_path)
						with open(file_name+"_G_"+str(filecounter)+".dssp", "a") as g:
								print(set_line_header+"\n"+line+"\n",file=g)
								g.close()
	else:
		continue
print("The output is provided in shortH_output directory.")

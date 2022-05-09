#!/usr/bin/env python3

import os
import os.path
import pathlib
import sys
import glob
import sys, time, os



dssp_path = os.getcwd()+"/longH_output"

dssp_files = os.listdir(dssp_path)
helix_start = "0"
helix_end = "0"

out_file = open("start_end.csv", 'a')
out_file.write("helix,helix_start,helix_end\r")
            
for helix in dssp_files:
    with open(os.path.join(dssp_path, helix), 'r') as src_file:

            i = 0
            for line in src_file:

                line_array =  line.split()

                if len(line.split()) == 0:
                    continue

                i = i + 1

                if(i==1):
                    continue

                if(i==2):
                    helix_start = line_array[1]
                    #print(line_array[1])

                helix_end = line_array[1]


            print("Helix Name: "+helix+" Start: "+helix_start+", Helix End: "+helix_end)

            
            out_file.write(helix+","+helix_start+","+helix_end+"\r")

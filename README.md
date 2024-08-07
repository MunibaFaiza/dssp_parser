# DSSP file Parser - Python package to parse DSSP files to extract all helices from .dssp files

### Introduction

This package parses DSSP files and gives you all helices in separate files. Requires Python3

## Prepare your files

Save all DSSP files of the PDB structures in 'dssp_files' direcotry. These files can be obtained from the PDB structures using DSSP.

Test data is provided in the given directories.

### Usage

```$ python3 parse_longH_dssp.py```

```$ python3 parse_shortH_dssp.py```

The program will fetch all long helices denoted by 'H' in longH_output direcotry and all short ones (denoted by 'G') in shortH_output direcotry.

You can also find start and end residues of each helix using the script "start_end_hel.py".

```$ python3 start_end_helix_res.py```

The output is provided in "start_end.csv" file.

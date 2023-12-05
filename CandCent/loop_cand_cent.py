import os, sys

# Loop of cand_cent.py to obtain all centromeres of a list of species in a row
# How to run: python3 loop_cand_cent.py files_list
# Files_list with 2 columns (genome_file + output_file) separated with tab
# You can see example of files_list in: files_list.txt
# Output example: Pf3D_cent.fasta

listafiles = open(sys.argv[1], "r").readlines()

for linea in listafiles:
	genome_file = (linea.split("\t")[0]).strip()
	output_file = (linea.split("\t")[1]).strip()
	
	os.system("python3 cand_cent.py " + genome_file + " > " + output_file)
	print(output_file + " created")
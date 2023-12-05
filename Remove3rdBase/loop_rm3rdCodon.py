import os, sys

# Loop for the script rm3rdCodon.py
# How to run: python3 loop_rm3rdCodon.py lista_codonFam.txt
# Input file with list of location of alignments
# Input example: lista_codonFam.txt

listafiles = open(sys.argv[1], "r").readlines()

for linea in listafiles:
	fam_file = (linea.split("\t")[0]).strip()
	
	os.system("python3 rm3rdCodon.py " + fam_file)

print("\n")
print("DONE")
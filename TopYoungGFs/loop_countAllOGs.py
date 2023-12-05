import os, sys

# loop for the script "countAllOGs.py"
# how to run: python3 loop_countAllOGs.py list_files_loopAllOGs.txt

lista = open(sys.argv[1], "r").readlines()

for linea in lista:
	agFile = (linea.split("\t")[0]).strip()
	tenOGsFile = (linea.split("\t")[1]).strip()
	tenOGsfullnames = (linea.split("\t")[2]).strip()	# With region names SUBTEL,INTERN,CONSERV
	tenOGsnonames = (linea.split("\t")[3]).strip()	# Without names, only OGs and seqs number per region

	# To obtain the 2 output files: with and without region names
	os.system("python3 countAllOGs.py " + agFile + " " + tenOGsFile + " " + tenOGsfullnames + " " + tenOGsnonames)
	print("\n") 
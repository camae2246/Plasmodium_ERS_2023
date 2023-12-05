import os, sys

# loop for the script "countOGs.py"
# how to run: python3 loop_count_OGs.py list_loop_countOGs.txt

lista = open(sys.argv[1], "r").readlines()

for linea in lista:
	yrFile = (linea.split("\t")[0]).strip()
	allOGs = (linea.split("\t")[1]).strip()
	tenOGs = (linea.split("\t")[2]).strip()

	# Para correr young_genes.py
	os.system("python3 countOGs.py " + yrFile + " " + allOGs + " " + tenOGs)
	print("\n") 
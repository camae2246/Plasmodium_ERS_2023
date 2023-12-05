import os, sys

# loop for the script "young_genes.py"
# how to run: python3 loop_young_genes.py list_loop_genesfunction.txt
# List example included: list_loop_genesfunction.txt

lista = open(sys.argv[1], "r").readlines()

for linea in lista:
	ysFile = (linea.split("\t")[0]).strip()
	yiFile = (linea.split("\t")[1]).strip()
	mapFile = (linea.split("\t")[2]).strip()
	ogFile = (linea.split("\t")[3]).strip()
	gfFile = (linea.split("\t")[4]).strip()
	output = (linea.split("\t")[5]).strip()

	# Para correr young_genes.py
	os.system("python3 genes_function.py " + ysFile + " " + yiFile + " " + mapFile + " " + ogFile + " " + gfFile + " " + output)
	print("\n") 
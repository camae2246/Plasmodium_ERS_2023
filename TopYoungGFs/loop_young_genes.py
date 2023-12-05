import os, sys

# loop for the script "young_genes.py"
# how to run: python3 loop_young_genes.py list_loop_younggenes.txt

lista = open(sys.argv[1], "r").readlines()

for linea in lista:
	archivo_ysfile = (linea.split("\t")[0]).strip()
	archivo_yifile = (linea.split("\t")[1]).strip()
	mapFile = (linea.split("\t")[2]).strip()
	ogFile = (linea.split("\t")[3]).strip()
	output = (linea.split("\t")[4]).strip()

	# Para correr young_genes.py
	os.system("python3 young_genes.py " + archivo_ysfile + " " + archivo_yifile + " " + mapFile + " " + ogFile + " " + output)
	print("\n") 
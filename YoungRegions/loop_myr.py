import os, sys

# loop for the script "modify_young_regions.py"
# how to run: python3 loop_myr.py lista_loop_myr.txt
# Example of list for running loop: lista_loop_myr.txt
# List format: ysFile + tab + yiFile + tab + ysFile_new + tab + yiFile_new

lista = open(sys.argv[1], "r").readlines()

for linea in lista:
	input_ysfile = (linea.split("\t")[0]).strip()
	input_yifile = (linea.split("\t")[1]).strip()
	new_ysfile = (linea.split("\t")[2]).strip()
	new_yifile = (linea.split("\t")[3]).strip()

	#Converting alignment to nucleotides
	os.system("python3  modify_young_regions.py " + input_ysfile + " " + input_yifile + " " + new_ysfile + " " + new_yifile)
	print("\n") 
import os, sys

# Script to get list of genes classified in regions (conserved, subtelomeric, internal)
# Subtelomeric regions are divided in right (RSUBTEL) and left (LSUBTEL)
# how to run: python3 young_genes.py ysFile yiFile mapFile OGFile yrFile
# Input and Output (1 & 2) examples in folder "ExamplesYoungGenes"
# Output: yrFile

ysFile = open(sys.argv[1], "r").readlines()
yiFile = open(sys.argv[2], "r").readlines()
mapFile = open(sys.argv[3], "r").readlines()[1:]
ogFile = open(sys.argv[4], "r").readlines()
yrFile = open(sys.argv[5], "w")

intervals = [*range(1,10000001,1000)]

# Here we're creating a dictionary with protein name as keys and OG (family) as values
og = {}
for linea in ogFile:
	gfname = (linea.split(",")[0]).strip()
	seqname = (linea.split(",")[1]).strip()			
	
	# Defining species 10-digit code and protein name from seqname
	especie = (seqname[:10]).strip()
	proteina = (seqname[11:]).strip()
	
	# Create a dictionary with proteina as keys and gfname as values		
	og[proteina] = gfname

# for k,v in og.items():
# 	print(k,[v])

# Here we're creating the dictionary for the subtelomeric young regions
ys = {}
for l in ysFile:
	l = l.strip()
	chr = (l.split(",")[0])
	lstart = (l.split(",")[1])
	lend = (l.split(",")[2])
	rstart = (l.split(",")[3])
	rend = (l.split(",")[4])
	
	if lstart != "na":	
		lstart = int(lstart)
	if lend != "na":
		lend = int(lend)
	if rstart != "na":
		rstart = int(rstart)
	if rend != "na":	
		rend = int(rend)
	
	inter = [lstart,lend,rstart,rend]
	ys[chr] = inter

# for k,v in ys.items():
# 	print(k)
# 	print(v)

# Here we're creating the dictionary for the internal young regions
yi = {}
for i in yiFile: yi[i.split(",")[0]] = []
for i in yiFile:
	chr = (i.split(",")[0])
	start = int(i.split(",")[1])
	end = int(i.split(",")[2])
	
	yi[chr].append(start)
	yi[chr].append(end)

# print(yi)

# Here we're defining if the proteins are located within the young regions
for p in mapFile:
	chr = (p.split(",")[0])
	start = int((p.split(",")[1]))
	end = int(p.split(",")[2])
	protein = (p.split(",")[3])
	oldtree = (p.split(",")[4])	# We don't need this info 
	
	for n in intervals: 
		next = int(n) + 1000
		if start >= n and start < next: 
			nstart = n
# 			info = [int(chr),nstart]
		if end >= n and end < next: 
			nend = n
# 			info.extend([nend])
#			mp[protein] = info
# 			print(chr + "," + str(nstart)  + "," + str(nend)  + "," + protein )
	
	category = "CONSERV"
	tree = []

	for k,v in yi.items():
		vm = list(v)
		if chr == k:				
			for i in range(0,len(vm),2):		
				li = i
				ls = i+1
# 				print(chr,str(j[li]),str(j[ls]))
				if nstart >= vm[li] and nstart <= vm[ls]:
					category = "INTERN"
					
	if category != "INTERN":	
		for schr in ys.keys():
			if chr == schr:
				if ys[chr][0] != "na":
					if nstart <= int(ys[chr][1]):
						category = "LSUBTEL"
								
				if ys[chr][2] != "na":
					if nstart >= int(ys[chr][2]):
						category = "RSUBTEL"
	
	if protein in og.keys():
		tree = og[protein]
	else:
		tree = "no_tree"

	out = "%s,%s,%s,%s,%s" % (chr,str(nstart),protein,tree,category)
	
	# OUTPUT 1: Complete gene list with all types of regions (including CONSERV)
	print(out)
	yrFile.write(out + "\n")
	
	# OUTPUT 2: Gene list with only young regions (LSUBTEL, INTERN, RSUBTEL)
# 	if category != "CONSERV":
# 		print(out)
# 		yrFile.write(out + "\n")
	

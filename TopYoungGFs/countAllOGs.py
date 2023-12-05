import os, sys

# Script for getting the top 10 GFs with highest number of seqs in young regions
# how to run: python3 countOGs.py Pf3D_allgenes.txt Pf3D_tenOGs.txt Pf3D_tenOGs_fullnames.txt Pf3D_tenOGs_nonames.txt
# Input and output examples in folder "ExamplesCountAllOGs"

agFile = open(sys.argv[1], "r").readlines()
tenOGsFile = open(sys.argv[2], "r").readlines()

# Output with names of regions
fullnamesOGs = open(sys.argv[3], "w")
# Output without names of regions
nonamesOGs = open(sys.argv[4], "w")

# Create dictionary with OGs from list with only young genes 
og = {}
for l in tenOGsFile:
	r = (l.split("\t")[0]).strip()
	family = (r.split(",")[0]).strip()
	number = (r.split(",")[1]).strip()
	
	og[family] = number

# for k,v in og.items():
# 	print(k, [v])		

# Count how many times each family is present in young regions
# It also calculates number of seqs per family present in conserved regions
families = {}
test = {}

for line in agFile: test[line.split(",")[3]] = []
for line in agFile:
	words = line.split(",")
	tree = words[3]
	category = words[4].strip()
	
	if tree in families:
		families[tree] = families[tree] + 1
	else:
		families[tree] = 1	

	if tree in test.keys():
		if category == "LSUBTEL":
			test[tree].append(category)		 		
		if category == "INTERN":
			test[tree].append(category)
		if category == "RSUBTEL":
			test[tree].append(category)	
		if category == "CONSERV":
			test[tree].append(category)	

newd = {}
for k,v in test.items():
	vm = list(v)
	vn = list(set(v))
	if k != "no_tree":
		c1 = 0
		c2 = 0
		c3 = 0
		for i in vm:
			if i == "LSUBTEL":
				c1 = c1 + 1
			
			if i == "INTERN":
				c2 = c2 + 1

			if i == "RSUBTEL":
				c1 = c1 + 1
			
			if i == "CONSERV":
				c3 = c3 + 1
		
# 		print(k, vn)
		info = [c1,c2,c3]
		newd[k] = info
		
# for k,v in newd.items():
# 	print(k, [v])		
		
# Print top 10 OGs list with name of regions and number of seqs per region
for key,vals in sorted(families.items(), key=lambda kv: kv[1], reverse=True):
	if key != "no_tree" and int(vals) >= 2:
		if key in newd.keys():		
			if key in og.keys():		
				out = "%s,%s\t%s,%s\t%s,%s\t%s,%s" % (key, vals,"SUBTEL",newd[key][0],"INTERN",newd[key][1],"CONSERV",newd[key][2])
				print(out)
				fullnamesOGs.write(out + "\n")

print("\n")

# Print top 10 OGs list without etiquetes - only number of seqs per region
for key,vals in sorted(families.items(), key=lambda kv: kv[1], reverse=True):
	if key != "no_tree" and int(vals) >= 2:
		if key in newd.keys():
			if key in og.keys():		
				out = "%s\t%s\t%s\t%s\t%s" % (key, newd[key][0], newd[key][1], newd[key][2], vals)
# 				out = "%s,%s" % (key, vals)
				print(out)
				nonamesOGs.write(out + "\n")

print("\n")

import os, sys

# Script for getting the list of OGs in young regions 
# Specifies how many sequences per type of young region each family has
# how to run: python3 countOGs.py Pf3D_YoungRegions.txt Pf3D_allOGs.txt Pf3D_tenOGs.txt

yrFile = open(sys.argv[1], "r").readlines()

# Complete list of OGs in young regions
allOGs = open(sys.argv[2], "w")
# Only list of top 10 OGs in young regions
only10OGs = open(sys.argv[3], "w")

# Count how many times a family is present in young regions
families = {}
test = {}

for line in yrFile: test[line.split(",")[3]] = []
for line in yrFile:
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
				c3 = c3 + 1
		
# 		print(k, vn)
		info = ["LSUBTEL", c1, "INTERN", c2, "RSUBTEL", c3]
		newd[k] = info
		
# for k,v in newd.items():
# 	print(k, [v])		
		
# # Print gene families (one per row) from highest to lowest value
# To get allOGs file
for key,vals in sorted(families.items(), key=lambda kv: kv[1], reverse=True):
	if key != "no_tree" and int(vals) >= 2:
		if key in newd.keys():		
			out = "%s,%s\t%s,%s\t%s,%s\t%s,%s" % (key, vals, newd[key][0], newd[key][1], newd[key][2], newd[key][3], newd[key][4], newd[key][5])
			print(out)
			allOGs.write(out + "\n")

print("\n")

# # To obtain the top 10 families (one per row) with the highest number of ocurrences
# To get only10OGs file
for key,vals in sorted(families.items(), key=lambda kv: kv[1], reverse=True)[:11]:
	if key != "no_tree" and int(vals) >= 2:
		if key in newd.keys():		
			out = "%s,%s\t%s,%s\t%s,%s\t%s,%s" % (key, vals, newd[key][0], newd[key][1], newd[key][2], newd[key][3], newd[key][4], newd[key][5])
# 			out = "%s,%s" % (key, vals)
			print(out)
			only10OGs.write(out + "\n")

print("\n")

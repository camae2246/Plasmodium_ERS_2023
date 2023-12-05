import os, sys

# Script to filter and select young regions based on max. and min. lenght
# How to run: python3 modify_young_regions.py ysFile yiFile newysFile newyiFile
# Example of input files: Pf3D_ysfile.txt (subtelomeres) and Pf3D_yifile.txt (internal)
# Example of output: Pf3D_ysfile_new.txt (subtelomeres) and Pf3D_yifile_new.txt (internal)

ysFile = open(sys.argv[1], "r").readlines()
yiFile = open(sys.argv[2], "r").readlines()
newysFile = open(sys.argv[3], "w")
newyifile = open(sys.argv[4], "w")

ys = {}
ys_na = {}

# To obtain the two subtelomeric young regions per chr
for l in ysFile:
	chr = (l.split(",")[0])
	lstart = int((l.split(",")[1])) # Start of chr
	lend = int(l.split(",")[2]) # Subtract 1000 to exclude the interval of the 2nd conserved gene
	rstart = int(l.split(",")[3])+1 # to exclude the interval of the 2nd conserved gene
	rend = int((l.split(",")[4]))	# End of chr
	
	# En caso de querer limitar las regiones subtelomericas a max. 200 kb
# 	if lend-lstart >= 200000:
# 		lend = lstart +199000
# 	if rend-rstart >= 200000:
# 		rstart = rend -199000
	
	inter = [lstart,lend,rstart,rend]
	ys[chr] = inter
	
	# if regions < 79000, leave out the region and put "na"
	if lend-lstart < 79000:
		lend = "na"
		lstart = "na"	
	if rend-rstart < 79000:
		rend = "na"
		rstart = "na"	
	
	inter_na = [lstart,lend,rstart,rend]
	ys_na[chr] = inter_na

# for k,v in ys.items():
# 	print(k, [*v])
# 
# print("\n")
# 
# for k,v in ys_na.items():
# 	print(k, [*v])
	
	
	# To write ysfile_new.txt	
	print(chr + "," + str(lstart) + "," + str(lend) + "," + str(rstart) + "," + str(rend).strip())
	newysFile.write(chr + "," + str(lstart) + "," + str(lend) + "," + str(rstart) + "," + str(rend).strip() + "\n")

print("\n")

# To obtain list of internal young regions per chr
yi = {}
for i in yiFile:
	chr = (i.split(",")[0])
	start = int((i.split(",")[1]))
	end = int(i.split(",")[2])-999
	
# 	print(chr + "," + str(start) + "," + str(end))
	
	status = "YES"
	
	# To avoid overlap between subtelomeric and internal young regions
	if chr in ys_na.keys():
		if ys_na[chr][1] != "na":
			if start == int(ys_na[chr][1]):
				start = int(ys_na[chr][1]) +1000
				if end-start >= 79000:
					status = "YES"
	
			if start > int(ys_na[chr][1]):
				if end-start >= 79000:
					status = "YES"
					
			if end <= int(ys_na[chr][1]):
				status = "NO"

		if ys_na[chr][2] != "na":
			if end >= int(ys_na[chr][2]):
				end = int(ys_na[chr][2]) -1000
				if end-start >= 79000:
					status = "YES"
			
			if start >= int(ys_na[chr][2]):
				status = "NO"		

	# Print final list of young regions and save it in yifile_new.txt
	if status == "YES":
		out = "%s,%s,%s" % (chr, str(start), str(end))
		print(out)
		newyifile.write(out + "\n")	
				
print("\n")


import os,sys
from Bio import SeqIO

# Script to analyze the chr. sequence with sliding window method to evaluate the GC content
# Output: Biggest chromosomic regions with highest AT content (Candidate centromere)
# How to run: python3 cand_cent.py genome_file
# You can see example of genome_file in: Pf3D_genome.fasta
# Output example: Pf3D_cent.fast

# If you want to obtain the centromeres of all species, run the loop file instead
# See info on loop file: loop_cand_cent.py

genome_file = sys.argv[1]

for cs in SeqIO.parse(genome_file, "fasta"):
	id_s = str(cs.id)
	se_s = str(cs.seq)
#	print(se_s)
	c = 0
	inter = (len(se_s)-99)
	ats = []
	inters = []
	int_dict = {}
	conc = "n"
	candCentromer = ""

	# Define 100-length intervals advancing by 1 nucleotide at a time
	for i in range(0,int(inter)):
		int_s = se_s[c : c+100]
		c = c+1
		# print(int_s)
		
		#GC and AT content
		gc_c = 0
		at_c = 0
		
		for n in int_s: 
			if n == "C": gc_c += 1
			if n == "G": gc_c += 1
			if n == "A": at_c += 1
			if n == "T": at_c += 1
		at_cp = (at_c/100)*100
		ats.append(int(at_cp))
# 		int_dict[int_s] = int(at_cp)
# 		print(int_dict.items())
		
		#Intervalos con gc_cp (GC content) igual o mayor a 90%
		#Intervals with gc_cp (GC content) equal or greater than 90% 
		#You can change this number in line below
		if at_cp >= 90: 
			if conc != "y":
				lf = i
			conc = "y"
		else: 
			if candCentromer != "" :
				conc = "s"
			else:
				conc = "n"
		
# 		while conc == "y": 
		if conc == "y":
			candCentromer += int_s[0] # Create seq with first nctd of intervals
		if conc == "s":
			if len(candCentromer) > 5:
				candCentromer += int_s[1:-1]
				ll = i + 99
				int_dict[str(lf) + "," + str(ll)] = candCentromer
			candCentromer = ""
   
	biggest_locus = sorted(int_dict, key=lambda k: len(int_dict[k]), reverse=True)[0]
	dict_fixed = sorted(int_dict, key=lambda k: len(int_dict[k]), reverse=True)
	biggest_seq = int_dict[biggest_locus]
	
	#Obtain AT content (%) of obtained candidate centromeric sequence
	at_fcount = 0
	for nucleotide in biggest_seq:
		if nucleotide == "A": at_fcount += 1
		if nucleotide == "T": at_fcount += 1
	at_final = round(((at_fcount/len(biggest_seq))*100), 2)
	
	#Print results in fasta format
	print("%s%s_(%s)_%s_%s\n%s" % (">", id_s, biggest_locus, len(biggest_seq), at_final, biggest_seq))
	
	#Print complete dictionary of candidate centromere regions
# 	print("%s\n%s" % (id_s, int_dict.keys()))   

import os,sys
from Bio import SeqIO
import re
from statistics import mean 

# Script for removing the 3rd base of codons in alignments
# How to run: python3 rm3rdCodon.py alingment_file
# Input example: OG0001325_codonaln.fa
# Output example: OG0001325_ModAlign.fa


genome_file = sys.argv[1]

# Name of new alignment file (Change this depending on the file name and location)
name = genome_file[0:9] + "_ModAlign.fa"

# Create folder for new alignments
# Change path for new alignments in LINE BELOW
nfolder_path = "/Users/camae/Thesis/GitHub/Plasmodium_ERS_2023_1/Remove3rdBase/Examples"
if not os.path.isdir(nfolder_path):
   os.makedirs(nfolder_path)

n_file = str(nfolder_path) + "/" + name
print(n_file)
f_file = open(n_file, "w")

for cs in SeqIO.parse(genome_file, "fasta"):
	id_s = str(cs.id)
	se_s = str(cs.seq)
# 	print(id_s + "\n" + se_s)
	c = 0
	n_codon = (len(se_s)/3) # Define number of codons
# 	print(id_s + "\n" + str(inter))
	new_seq = []
	nbase1 = []
	nbase2 = []
	nbase3 = []
	
	# Remove 3rd base of codons
	for i in range(0, int(n_codon)):
		codon = se_s[c:c+3] # Define number of bases per codon
		c = c+3 # Advance by 3 bases (that is, by codon)
		new_codon = codon[0] + codon[1] + "-"
		new_seq.append(new_codon) # Create list with new codons (without 3rd base)
		final_seq = "".join(new_seq) # Create string from list
	
	print(">%s\n%s" % (id_s, final_seq))
	f_file.write(">%s\n%s\n" % (id_s, final_seq))	
# Plasmodium_ERS_2023
Scripts for my research on Ectopic Recombination of Subtelomeres in Plasmodium

- cand_cent.py:
Analyzes all the chromosome sequences of a species with the sliding window method to evaluate the GC content.
Then, it retrieves a list of the largest chromosomal regions exhibiting the highest AT content (potential candidate centromeres for a species). 
How to run: python3 cand_cent.py genome_file
Genome_file example: Pf3D_genome.fasta
Output example: Pf3D_cent.fast
If you want to analyze multiple species at once, run: loop_cand_cent.py (see script for more details)

- get_young_regions.rb:
Retrieves the subtelomeric and internal young regions (unrefined)
To get subtelomeric young regions: Choose telomere window
To get internal young regions: Choose internal window
Input file example: Pf3D_database.txt
Input file format: based on Pf3D_freqs4maps.csv (example included) obtained with PhyloChromoMap
Input file with information of the presence of gene families per chromosome intervals
In this file, a gene family is considered present if it is found in more than 0.25 minor clades per major clade (1 for presence, 0 for absence)

- modify_young_regions.py:
Filters, selects and refines subtelomeric and internal young regions based on established maximum and minimum lenght.
How to run: python3 modify_young_regions.py ysFile yiFile newysFile newyiFile
ysFile: File with chromosome number and subtelomeric young regions (a chromosome per row)
yiFile: File with chromosome number and internal young regions (a region per row)
Output files: newysFile (subtelomeres) and newyiFile (internal)
Example of input files: Pf3D_ysfile.txt and Pf3D_yifile.txt
Example of output: Pf3D_ysfile_new.txt and Pf3D_yifile_new.txt
If you want to analyze multiple species at once, run: loop_myr.py (see script for more details)

- young_genes.py:
Retrieves a list of genes classified in chromosomic regions (conserved, subtelomeric, internal)
Subtelomeric regions are divided in right (RSUBTEL) and left (LSUBTEL)
How to run: python3 young_genes.py ysFile yiFile mapFile OGFile yrFile
ysFile and yiFile: Files with subtelomeric and internal young regions list, respectively
mapFile: mapping file
OGFile: List of sequences per gene family (OG) - One sequence per row
yrFile: Output file
Input and Output (1 & 2) examples in folder "ExamplesYoungGenes"
If you want to analyze multiple species at once, run: loop_young_genes.py (see script for more details)

- countOGs.py:
Analyzes all gene families (OGs) of a species a retrieves a list of OGs in young regions (1 OG per row)
It also specifies the number of sequences per type of young region for each gene family
and organizes them from the highest to the lowest based on the number of sequences in young regions
How to run: python3 countOGs.py Pf3D_YoungRegions.txt Pf3D_allOGs.txt Pf3D_tenOGs.txt
Input file: Pf3D_YoungRegions.txt
Output files: Pf3D_allOGs.txt (list of all OGs) and Pf3D_tenOGs.txt (list of top 10 OGs)
Input and output examples in folder “ExamplesCountOGs”
If you want to analyze multiple species at once, run: loop_countOGs.py (see script for more details)

- countAllOGs.py:
Retrieves the top 10 OGs with highest number of seqs in young regions
It also specifies the number of sequences per type of chromosomic region (CONSERV, RSUBTEL, LSUBTEL, INTERN)
How to run: python3 countOGs.py Pf3D_allgenes.txt Pf3D_tenOGs.txt Pf3D_tenOGs_fullnames.txt Pf3D_tenOGs_nonames.txt
Input files: Pf3D_allgenes.txt Pf3D_tenOGs.txt
Output files: Pf3D_tenOGs_fullnames.txt (with name of regions) Pf3D_tenOGs_nonames.txt (without name of regions)
Input and output examples in folder "ExamplesCountAllOGs"
If you want to analyze multiple species at once, run: loop_countAllOGs.py (see script for more details)

- genes_function.py:
Retrieves a gene list (one sequence per row) with region category (CONSERV, RSUBTEL, LSUBTEL, INTERN) and protein info (product name).
How to run: python3 young_genes.py ysFile yiFile mapFile ogFile gfFile newFile
ysFile and yiFile: Files with subtelomeric and internal young regions list, respectively
mapFile: mapping file
ogFile: List of sequences per gene family (OG) - One sequence per row
gfFile: List of sequences with product name - One sequence per row
How to run (with example files): python3 young_genes.py Pf3D_ysfile_new.txt Pf3D_yifile_new.txt Pf3DMapFile.csv Pf3DAllGenesList.txt Pf3D_genesfunction.txt Pf3D_allgenes_function.txt
Input and output examples in folder "ExamplesGeneFunction"
If you want to analyze multiple species at once, run: loop_genes_function.py (see script for more details)

- rm3rdCodon.py
Removes the 3rd base of codons in alignments and creates a file with modified alignments in fasta format.
How to run: python3 rm3rdCodon.py alingment_file
Input example: OG0001325_codonaln.fa
Output example: OG0001325_ModAlign.fa
If you want to analyze and modify multiple alignments at once, run: loop_rm3rdCodon.py (see script for more details)

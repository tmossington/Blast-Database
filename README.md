# Blast-Database

This program requires the following packages:

BioPython (https://biopython.org)
PySAM (https://github.com/pysam-developers/pysam)
SQLObject (http://sqlobject.org)
NCBI Blast (https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&amp;PAGE_TYPE=BlastDocs&amp;DOC_TYPE=Download)
PyMol (https://pymol.org/2/)


This program computes all pairwise blast alignments for two species' proteomes and pulls out orthologous pairs. 

This program computes all pairwise blast alignments for two species' proteomes and stores the alignments in a relational database. 
It is capable of retrieving the blast alignment for two proteins (specified by their accession numbers) from the relational database and 
finds pairs of orthologous proteins that are mutually best hits.
The blast analysis will take several hours, which is why it is split into two separate files. 

1. SET UP:

Prior to running blast, each fasta file must be prepared in the steps below:

A. create a folder called "blastdb"

B. download your 2 fasta files and place them inside the blastdb folder

C. if compressed, extract each fasta file manually, or from the terminal:
    cd blastdb
    gunzip *.gz
    ls -l

D. To format:
    cd blastdb
    ls -l
    makeblastdb -help
    makeblastdb -in query.fasta -dbtype prot
    makeblastdb -in reference.fasta -dbtype prot
    ls -l
    
NOTE: query and reference refers to the two species' fasta files, one of which will be used as a query against the other. It does not matter which species acts as the query or reference.
    
These steps should create several new files needed for the blast analysis. No further alterations on these files is neccessary.

2. RUNNING BLAST:

python3 blast.py query.fasta reference.fasta

and

python3 blast2.py query.fasta reference.fasta

Running the two blast programs will output 2 xml files (alignment_query.xml) and (alignment_reference.xml) (make sure to change line 21 in each blast file using your chosen species instead of query and reference)

3. Parsing data into relational database:

python3 protein_parse.py query.fasta reference.fasta

This will parse data from both fasta files and the two blast alignments into a single relational database. (Be sure to change lines 51 and 74 to the correct xml file names)


4. Retrieving an alignment
retrieve.py is used to retrieve the blast alignment score for any two accession numbers specified on the command line. 

run:

python3 retrieve.py accession1 accession2

The accession numbers cannot be from the same species, one must be from the query and one from the reference.

5. Finding all orthologs:

besthit.py pulls the best score from each query protein and if the query and reference proteins are mutually best hits 
(the best pair for the query is the reference, and the best pair for the reference is the query), then it prints that pair out.

run:

python3 besthit.py

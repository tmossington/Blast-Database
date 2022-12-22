# Blast-Database
This program computes all pairwise blast alignments for two species' proteomes and pulls out orthologous pairs

This program computes all pairwise blast alignments for two species' proteomes and stores the alignments in a relational database. 
It is capable of retrieving the blast alignment for two proteins (specified by their accession numbers) from the relational database and 
finds pairs of orthologous proteins that are mutually best hits.

The blast analysis will take several hours, which is why it is split into two separate files. 
When you have the two fasta files of your chosen proteomes, you run blast.py on the first one and blast2.py on the second one. 
After blast has been run, protein_parse.py parses the information from the xml file into a db3 file.

retrieve.py is used to retrieve the blast alignment score for any two accession numbers specified on the command line.

besthit.py pulls the best score from each query protein and if the query and reference proteins are mutually best hits 
(the best pair for the query is the reference, and the best pair for the reference is the query), then it prints that pair out.

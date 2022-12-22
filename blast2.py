# Write a program that computes all pairwise blast alignments for two species’ proteomes and stores the alignment in a relational database

from Bio.Blast.Applications import NcbiblastpCommandline
from model import *
import sys
import Bio.SeqIO
from Bio.Blast import NCBIXML
init()


# Blast 2
blast_prog = '/Users/tmossington/ncbi-blast-2.13.0+/bin/blastp'
blast_query = (sys.argv[2])
blast_db = (sys.argv[1])

# Build the command line
cmdline = NcbiblastpCommandline(cmd=blast_prog,
								query=blast_query,
								db=blast_db,
								outfmt=5,
								out="alignment_drosoph2.xml")

# execute
stdout, stderr = cmdline()
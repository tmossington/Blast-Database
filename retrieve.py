# Write a program that retrieves the blast alignment for two proteins (specified by their accessions) from the relational database

import sys
from model import *
init()


try:
	query = (sys.argv[1])
except IndexError:
	print("Need a query accession number", file=sys.stderr)
	sys.exit(1)

try:
	reference = (sys.argv[2])
except IndexError:
	print("Need a reference accession number", file=sys.stderr)
	sys.exit(1)
	

try:
	p = Proteins.byAccession(query)
except SQLObjectNotFound:
	print("Accession number",query,"does not exist in this database",file=sys.stderr)
	sys.exit(1)
	
qid= (p)	

	
try:
	p = Proteins.byAccession(reference)
except SQLObjectNotFound:
	print("Accession number", reference, "does not exist in this database",file=sys.stderr)
	sys.exit(1)


rid = (p)
#print(qid, rid)

for a in (Alignments.select(Alignments.q.query == qid) and Alignments.select(Alignments.q.ref == rid)):
	if a.query == qid and a.ref == rid:
		print("***Alignment***\n\n",a.id,"Query accession: \n", a.query,"Reference accession: \n", a.ref,"E-value: \n", a.evalue)
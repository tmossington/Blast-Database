from Bio.Blast.Applications import NcbiblastpCommandline
from model import *
import sys
import Bio.SeqIO
from Bio.Blast import NCBIXML
init()

# Parse results by opening the output file
init(new=True)


seqfilename = sys.argv[1]

seqfile = open(seqfilename)
for seq_record in Bio.SeqIO.parse(seqfile, "fasta"):
	accession = seq_record.id
	desc = seq_record.description
	desc1 = desc.split('[')
	org1 = desc1[1].split(']')
	organism = org1[0]
	desc2 = desc1[0]
	description = desc2.split(' ', 1)
	gene = (description[1])
	#print("accession:", accession)
	#print("organism:", organism)
	#print("gene:", gene)
	
	p = Proteins(accession = accession, gene = gene, organism = organism)
seqfile.close()

seqfilename = sys.argv[2]

seqfile = open(seqfilename)
for seq_record in Bio.SeqIO.parse(seqfile, "fasta"):
	accession = seq_record.id
	desc = seq_record.description
	desc1 = desc.split('[')
	org1 = desc1[1].split(']')
	organism = org1[0]
	desc2 = desc1[0]
	description = desc2.split(' ', 1)
	gene = (description[1])
	#print("accession:", accession)
	#print("organism:", organism)
	#print("gene:", gene)
	
	p = Proteins(accession = accession, gene = gene, organism = organism)
seqfile.close()


result_handle = open("alignment_yeast2.xml")
for blast_result in NCBIXML.parse(result_handle):
	for alignment in blast_result.alignments:
		for hsp in alignment.hsps:
			if hsp.expect < 1e-5:
				q1 = (blast_result.query.split(' '))
				q2 = q1[0]
				#print("query: ",q2)
				ref1 = (alignment.title.split('|'))
				ref2= ref1[2].split(' ')
				ref3 = (ref2[1])
				#print("reference: ",ref3)
				evalue = (hsp.expect)
				#print(evalue)
				query = Proteins.byAccession(q2)
				ref = Proteins.byAccession(ref3)
					
					

				a = Alignments(query = query, ref = ref, evalue = evalue)
					
result_handle.close()

result_handle = open("alignment_drosoph2.xml")
for blast_result in NCBIXML.parse(result_handle):
	for alignment in blast_result.alignments:
		for hsp in alignment.hsps:
			if hsp.expect < 1e-5:
				q1 = (blast_result.query.split(' '))
				q2 = q1[0]
				#print("query: ",q2)
				ref1 = (alignment.title.split('|'))
				ref2= ref1[2].split(' ')
				ref3 = (ref2[1])
				#print("reference: ",ref3)
				evalue = (hsp.expect)
				#print(evalue)
				query = Proteins.byAccession(q2)
				ref = Proteins.byAccession(ref3)
					
					

				a = Alignments(query = query, ref = ref, evalue = evalue)
					
result_handle.close()




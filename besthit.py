# Write a program that finds pairs of orthologous proteins that are mutually best hits in the species’ proteomes

import sys
import sqlite3

conn = sqlite3.connect('protein_align2.db3')

q = {}

c = conn.cursor()
c.execute("""
	select query_id, ref_id, min(evalue)
	from Alignments
	group by query_id;
	""")

for row in c:
	q.update({(row[0],row[2]):(row[1],row[2])})


for k,v in q.items():
	v1 = v[0]
	k1 = k[0]
	e1 = k[1]
	for k,v in q.items():
		if v1 == k[0]:
			v2 = v[0]
			k2 = k[0]
			e2 = k[1]
			if k1 == v2 and v1 == k2:
				print(k1, v1, e1)
			
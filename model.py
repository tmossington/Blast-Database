from sqlobject import *
import os.path, sys

dbfile = 'protein_align.db3'

def init(new=False):
	conn_str = os.path.abspath(dbfile)
	conn_str = 'sqlite:'+ conn_str
	
	sqlhub.processConnection = connectionForURI (conn_str)
	if new:
		Proteins.dropTable(ifExists=True)
		Alignments.dropTable(ifExists=True)
		Proteins.createTable()
		Alignments.createTable()
		
		
class Proteins(SQLObject):
	accession = StringCol(alternateID=True)
	gene = StringCol()
	organism = StringCol()
	
	
class Alignments(SQLObject):
	query = ForeignKey("Proteins")
	ref = ForeignKey("Proteins")
	evalue = FloatCol()
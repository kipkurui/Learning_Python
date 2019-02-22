paths = raw_input("Enter a valid PATH for a PDB file: ")
PDBfile=open(paths,"r")

def parselen(string,noperline,indentation=0):
    seq = ""
    i = 0
    while i <len(string):
        seq+= " "*indentation+string[i:i+noperline]+"\n"
        i += noperline
    return seq


def extractTitle(PDBfile):
    title = "Title: "
    for line in PDBfile:
        if line.startswith("TITLE"):
            title += line[10:80].rstrip()
    return title

def add_to_PDBdict(PDB,key,seq):
    PDB[key]=seq
    return PDB

def extractHelix(PDBfile):
    title = "Title: "
    for line in PDBfile:
        if line.startswith("TITLE"):
            title += line[10:80].rstrip()
    return title

def countHelix(PDBfile,char):
    PDBfile.seek(0)
    count = 0
    for line in PDBfile:
        if line.startswith("HELIX")and line[32]==char:
            count+=1
    return count
def countSheet(PDBfile,char):
    PDBfile.seek(0)
    count = 0
    for line in PDBfile:
        if line.startswith("SHEET")and line[32]==char:
            count+=1
    return count
def extractSeq(PDBfile,char):
    PDBfile.seek(0)
    seq=""
    for line in PDBfile:
        if line.startswith("SEQRES")and line[11]==char:
            seq+=line[18:70]
    return seq
def oneto3(seq,dict):
    oneaa = ""
    for i in seq:
        if i !="":
            oneaa+=dict[i]
    return oneaa
def parseSequence(sequence,numberperline,indentation=0):
	seq=""
	index=0
	while index<len(sequence):
		seq += " "*indentation +sequence[index:index+numberperline] + "\n"
		index +=numberperline
	return seq
oneTO3 ={'VAL':'V', 'ILE':'I', 'LEU':'L', 'GLU':'E', 'GLN':'Q',
             'ASP':'D', 'ASN':'N', 'HIS':'H', 'TRP':'W', 'PHE':'F', 'TYR':'Y',
            'ARG':'R', 'LYS':'K', 'SER':'S', 'THR':'T', 'MET':'M', 'ALA':'A',
            'GLY':'G', 'PRO':'P', 'CYS':'C'}
seqA= extractSeq(PDBfile,"A")
print seqA.split(" ")
seqB= extractSeq(PDBfile,"B")
counthelixA= countHelix(PDBfile,"A")
countsheetA = countSheet(PDBfile,"A")
counthelixB= countHelix(PDBfile,"B")
countsheetB = countSheet(PDBfile,"B")
print oneto3(seqA.split(" "),oneTO3)
print oneto3(seqB.split(" "),oneTO3)
##PDB ={}
title = extractTitle(PDBfile)
seq= parselen(title,80)
##PDB =add_to_PDBdict(PDB,"Title",seq)

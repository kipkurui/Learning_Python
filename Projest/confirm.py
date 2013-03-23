paths = raw_input("Enter a valid PATH for a PDB file: ")
PDBfile=open(paths,"r")
def confirm():
    n=str(3)
    PDBfile.seek(0)
    for line in PDBfile:
        if line.startswith("SHEET") and line[9]==n and (line[13]=="B" or line[13]=="C"):
            print line
print confirm()

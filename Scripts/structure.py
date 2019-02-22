paths = raw_input("Enter a valid PATH for a PDB file: ")
PDBfile=open(paths,"r")
PDB = {'SequenceA': 'YNFFPRKPKWDKNQITYRIIGYTPDLDPETVDDAFARAFQVWSDVTPLRFSRIHDGEADIMINFGRWEHGDGYPFDGKDGLLAHAFAPGTGVGGDSHFDDDELWTLGKGVGYSLFLVAAHAFGHAMGLEHSQDPGALMAPIYTYTKNFRLSQDDIKGIQELYGASPD',
       'SequenceB': 'ISYGNDALMP', 'ThreeSeqA': ' TYR ASN PHE PHE PRO ARG LYS PRO LYS TRP ASP LYS ASN GLN ILE THR TYR ARG ILE ILE GLY TYR THR PRO ASP LEU ASP PRO GLU THR VAL ASP ASP ALA PHE ALA ARG ALA PHE GLN VAL TRP SER ASP VAL THR PRO LEU ARG PHE SER ARG ILE HIS ASP GLY GLU ALA ASP ILE MET ILE ASN PHE GLY ARG TRP GLU HIS GLY ASP GLY TYR PRO PHE ASP GLY LYS ASP GLY LEU LEU ALA HIS ALA PHE ALA PRO GLY THR GLY VAL GLY GLY ASP SER HIS PHE ASP ASP ASP GLU LEU TRP THR LEU GLY LYS GLY VAL GLY TYR SER LEU PHE LEU VAL ALA ALA HIS ALA PHE GLY HIS ALA MET GLY LEU GLU HIS SER GLN ASP PRO GLY ALA LEU MET ALA PRO ILE TYR THR TYR THR LYS ASN PHE ARG LEU SER GLN ASP ASP ILE LYS GLY ILE GLN GLU LEU TYR GLY ALA SER PRO ASP', 'ThreeSeqB': ' ILE SER TYR GLY ASN ASP ALA LEU MET PRO',
 'Title': 'Title: CRYSTAL STRUCTURE OF MMP-2 ACTIVE SITE MUTANT IN COMPLEX WITH APP- DRIVED\n DECAPEPTIDE INHIBITOR'}
def extractSrtA(PDBfile):
    PDBfile.seek(0)
    chainA = {}
    HelixA =[]
    SheetA = []
    for line in PDBfile:
        if line.startswith("HELIX")and line[19]=="A":
            HelixA += [(line[9],int(line[21:26].strip()),int(line[33:38].strip()))]
        if line.startswith("SHEET")and line[21]=="A":
            SheetA += [(line[9]+line[13],int(line[22:27].strip()),int(line[33:38].strip()))]
        chainA["HelixA"]=HelixA
        chainA["SheetA"]=SheetA
    return chainA

def extractSrtB(PDBfile):
    PDBfile.seek(0)
    ChainB = {}
    HelixB =[]
    SheetB = []
    for line in PDBfile:
        if line.startswith("HELIX")and line[19]=="B":
            HelixB += [(line[19]+line[9],int(line[20:26]),int(line[33:38].strip()))]
        if line.startswith("SHEET") and line[21]=="B":
            SheetB += [(line[13]+line[9],int(line[22:27]),int(line[33:38].strip()))]
        ChainB["HelixB"]=HelixB
        ChainB["SheetB"]=SheetB
    return ChainB
def parselen(string,noperline,indentation=0):
    seq = ()
    i = 0
    while i <len(string):
        seq+= (" "*indentation+string[i:i+noperline]+"\n",)
        i += noperline
    return seq
SequenceA =PDB["SequenceA"]
ChainA = extractSrtA(PDBfile)
s = "|"
h = "/"
helix =[]
sheet =[]
secStructure = ""
tagid = ""
taglist=[' ']*len(SequenceA)
structure=["-"]*len(SequenceA)
for i in ChainA["SheetA"]:
    a=(i[1]-1)
    b=i[2]
    structure[a:b] = s*((b-a))
for i in ChainA["HelixA"]:
    a=(i[1]-1)
    b=i[2]
    structure[a:b] = h*((b-a))

for i in ChainA["SheetA"]:
    a=(i[1]-1)
    b=i[2]
    taglist[a:a+1] = i[0]
for i in ChainA["HelixA"]:
    a=(i[1]-1)
    taglist[a:a+1] = i[0]
for i in structure:
    secStructure += i.strip()
for i in taglist:
    tagid += i

labels =parselen(tagid,80,indentation=0)
structure=parselen(secStructure,80,indentation=0)
sequences=parselen(SequenceA,80,indentation=0)
for i, j, k in zip(sequences,structure,labels):
    print i,j,k
print extractSrtB(PDBfile)
print extractSrtA(PDBfile)

ChainA={'SheetA': [('1A', 2, 3), ('2A', 128, 129), ('1B', 49, 52),
            ('2B', 14, 19), ('3B', 60, 65), ('4B', 96, 99),
            ('5B', 83, 86), ('1C', 104, 105), ('2C', 112, 113)],
 'HelixA': [('1', 27, 44), ('2', 114, 126), ('3', 151, 163)]}

{'HelixB': [], 'SheetB': [('B6', 7, 8)]}

PDB = {'SequenceA': 'YNFFPRKPKWDKNQITYRIIGYTPDLDPETVDDAFARAFQVWSDVTPLRFSRIHDGEADIMINFGRWEHGDGYPFDGKDGLLAHAFAPGTGVGGDSHFDDDELWTLGKGVGYSLFLVAAHAFGHAMGLEHSQDPGALMAPIYTYTKNFRLSQDDIKGIQELYGASPD',
       'SequenceB': 'ISYGNDALMP', 'ThreeSeqA': ' TYR ASN PHE PHE PRO ARG LYS PRO LYS TRP ASP LYS ASN GLN ILE THR TYR ARG ILE ILE GLY TYR THR PRO ASP LEU ASP PRO GLU THR VAL ASP ASP ALA PHE ALA ARG ALA PHE GLN VAL TRP SER ASP VAL THR PRO LEU ARG PHE SER ARG ILE HIS ASP GLY GLU ALA ASP ILE MET ILE ASN PHE GLY ARG TRP GLU HIS GLY ASP GLY TYR PRO PHE ASP GLY LYS ASP GLY LEU LEU ALA HIS ALA PHE ALA PRO GLY THR GLY VAL GLY GLY ASP SER HIS PHE ASP ASP ASP GLU LEU TRP THR LEU GLY LYS GLY VAL GLY TYR SER LEU PHE LEU VAL ALA ALA HIS ALA PHE GLY HIS ALA MET GLY LEU GLU HIS SER GLN ASP PRO GLY ALA LEU MET ALA PRO ILE TYR THR TYR THR LYS ASN PHE ARG LEU SER GLN ASP ASP ILE LYS GLY ILE GLN GLU LEU TYR GLY ALA SER PRO ASP', 'ThreeSeqB': ' ILE SER TYR GLY ASN ASP ALA LEU MET PRO',
 'Title': 'Title: CRYSTAL STRUCTURE OF MMP-2 ACTIVE SITE MUTANT IN COMPLEX WITH APP- DRIVED\n DECAPEPTIDE INHIBITOR'}
SequenceA =PDB["SequenceA"]
s = "|"
h = "/"
helix =[]
sheet =[]
null=[]
nul = ""
spa = ""
a = len(SequenceA)
print a
space=[]
space=[' ']*len(SequenceA)
null=["-"]*len(SequenceA)

for i in ChainA["SheetA"]:
    a=(i[1]-1)
    b=i[2]
    null[a:b] = s*((b-a))
for i in ChainA["HelixA"]:
    a=(i[1]-1)
    b=i[2]
    null[a:b] = h*((b-a))

for i in ChainA["SheetA"]:
    a=(i[1]-1)
    b=i[2]
    space[a:a+1] = i[0]
for i in ChainA["HelixA"]:
    a=(i[1]-1)
    space[a:a+1] = i[0]
for i in null:
    nul += i.strip()
for i in space:
    spa += i

def parselen(string,noperline,indentation=0):
    seq = ()
    i = 0
    while i <len(string):
        seq+= (" "*indentation+string[i:i+noperline]+"\n",)
        i += noperline
    return seq
labels =parselen(spa,80,indentation=0)
structure=parselen(nul,80,indentation=0)
sequences=parselen(SequenceA,80,indentation=0)
for i, j, k in zip(sequences,structure,labels):
    print i,j,k
##print helix
##Back-up
####if response.upper() =="S":
##    SequenceA =PDB["SequenceA"]
##    ChainA = extractSrtA(PDBfile)
##    s = "|"
##    h = "/"
##    helix =[]
##    sheet =[]
##    secStructure = ""
##    tagid = ""
##    taglist=[' ']*len(SequenceA)
##    structure=["-"]*len(SequenceA)
##    for i in ChainA["SheetA"]:
##        a=(i[1]-1)
##        b=i[2]
##        structure[a:b] = s*((b-a))
##    for i in ChainA["HelixA"]:
##        a=(i[1]-1)
##        b=i[2]
##        structure[a:b] = h*((b-a))
##    for i in ChainA["SheetA"]:
##        a=(i[1]-1)
##        b=i[2]
##        taglist[a:a+1] = i[0]
##    for i in ChainA["HelixA"]:
##        a=(i[1]-1)
##        taglist[a:a+1] = i[0]
##    for i in structure:
##        secStructure += i.strip()
##    for i in taglist:
##        tagid += i
##    labels =parselen2(tagid,80,indentation=0)
##    structure=parselen2(secStructure,80,indentation=0)
##    sequences=parselen2(SequenceA,80,indentation=0)
##    for i, j, k in zip(sequences,structure,labels):
##        print i,j,k
    

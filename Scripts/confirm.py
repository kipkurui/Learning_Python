paths = raw_input("Enter a valid PATH for a PDB file: ")
PDBfile=open(paths,"r")
def ectractSheetInfo():
    PDBfile.seek(0)
    SheetLists =[]
    for line in PDBfile:
        if line.startswith("SHEET"):
            SheetLists +=[[["strand:",line[8:10].strip()],["sheetID:",line[12:14].strip()],
                       ["numStrands",int(line[15:16])],["initResName:",line[17:20].strip()],
                       ["initChainID:",line[21:22].strip()],
                      ["initSeqNum:",int(line[23:26].strip())],["initICode:",line[26:27].strip()],
                      ["endResName:",line[27:31].strip()],["endChainID:",line[32:33].strip()],
                      ["endSeqNum:",int(line[34:37].strip())],["endICode:",line[37:38].strip()],
                      ["sense:",line[39:40].strip()],["curAtom:",line[42:45].strip()],
                       ["curResName:",line[45:48].strip()],["curChainId:",line[49:50].strip()],
                    ["curResSeq:",line[51:54].strip()],["curIcode:",line[54:55].strip()],
                      ["prevAtom:",line[57:60].strip()],["prevResName:",line[60:63].strip()],
                       ["prevChainId:",line[64:65].strip()],["prevResSeq:",line[66:69].strip()],
                       ["prevICode:",line[69:70].strip()]],]
    return SheetLists
def confirm():
    n=str(3)
    PDBfile.seek(0)
    for line in PDBfile:
        if line.startswith("SHEET") and line[9]==n and (line[13]=="B" or line[13]=="C"):
            print line
def extractSrtA(helixSheets):
    chainA = {}
    HelixA =[]
    SheetA = []
    for i in helixSheets["Helix"]:
        if i[3][1]=="A":
            HelixA += [[str(i[1][1])+str(i[3][1]),i[4][1],i[8][1]]]
    for i in helixSheets["Sheet"]:
        if i[4][1]=="A":        
            SheetA += [[str(i[0][1])+str(i[1][1]),i[5][1],i[9][1]]]
        chainA["HelixA"]=HelixA
        chainA["SheetA"]=SheetA
    return chainA

def extractSrtB(helixSheets):
    chainB = {}
    HelixB =[]
    SheetB = []
    for i in helixSheets["Helix"]:
        if i[3][1]=="B":
            HelixA += [[str(i[1][1])+str(i[3][1]),i[4][1],i[8][1]]]
    for i in helixSheets["Sheet"]:
        if i[4][1]=="B":        
            SheetB += [[str(i[0][1])+str(i[1][1]),i[5][1],i[9][1]]]
        chainB["HelixA"]=HelixB
        chainB["SheetA"]=SheetB
    return chainB
def extractHelixInfo():
    PDBfile.seek(0)
    HelixLists =[]
    for line in PDBfile:
        if line.startswith("HELIX"):
            HelixLists +=[[["serNum:",int(line[8:10].strip())],["helixID:",int(line[12:14].strip())],
                      ["initResName:",line[15:18].strip()],["initChainID:",line[19:20].strip()],
                      ["initSeqNum:",int(line[22:25].strip())],["initICode:",line[25:26].strip()],
                      ["endResName:",line[27:30].strip()],["endChainID:",line[31:32].strip()],
                      ["endSeqNum:",int(line[34:37].strip())],["endICode:",line[37:38].strip()],
                      ["helixClass:",int(line[39:40].strip())],["comment:",line[41:70].strip()],
                      ["length:",int(line[72:76].strip())]],]
    return HelixLists
helixSheets ={}
HelixLists=extractHelixInfo()
sheetLists=ectractSheetInfo()
helixSheets["Helix"]=HelixLists
helixSheets["Sheet"]=sheetLists
print extractSrtA(helixSheets)
print extractSrtB(helixSheets)

paths = raw_input("Enter a valid PATH for a PDB file: ")
PDBfile=open(paths,"r")
print "Choose one of the Manipulation Options: "
print "List(L)  Edit(E)  New(N)  Remove(R)  Main Menu(M)"
response = raw_input(":")
helixSheets ={}
if response.upper() == "L":
    response =raw_input("Do you want to list the Helix (H) or the Sheet (S): ")
    if response.upper() == "S":
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
        n = 1
        l=len(SheetLists)
        for i in SheetLists:
            print "Helix"+str(n)+"of"+str(l)+":"
            for j in i:
                print "  %-13s %s"% (j[0],str(j[1]).strip())
            n +=1
response =raw_input("Do you want to list the Helix (H) or the Sheet (S): ")
if response.upper() == "H":
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
    
    helixSheets["Helix"]=HelixLists
    n = 1
    l=len(HelixLists)
    for i in range(len(HelixLists)):
        print "Helix"+str(n)+"of"+str(l)+":"
        if HelixLists[i][10][1]=='1':
            HelixLists[i][10][1]="Right-handed alpha"
        for j in HelixLists[i]:
            if j[0] =="helixClass:" and j[1]==1:
                j[1]="Right-handed alpha"
            print "  %-13s %s"% (j[0],str(j[1]).strip())
        n +=1
helixSheets["Sheet"]=SheetLists
def countHelix(PDBfile,char): #use this to save the count of helix 
    PDBfile.seek(0)
    count = 0
    for line in PDBfile:
        if line.startswith("HELIX")and line[31]==char:
            count+=1
    return count
def countSheet(PDBfile,char):
    PDBfile.seek(0)
    count = 0
    for line in PDBfile:
        if line.startswith("SHEET")and line[32]==char:
            count+=1
    return count
helixClass={1:"Right-handed alpha",2:"Right-handed omega",3:"Right-handed pi",4:"Right-handed gamma",
            5:"Right-handed 3 - 10",6:"Left-handed alpha",7:"Left-handed omega",8:"Left-handed gamma",
            9:"2 - 7 ribbon/helix",10:"Polyproline"}
def edit(response,feature,action="edited"):
    if int(response)==int(response): #convert this as a function
        n= int(response)-1
        Helix= helixSheets[feature][n] #exraxt lists for Helix
        Helix[3][1]=raw_input(Helix[3][0]+str(Helix[3][1])) #chainID
        Helix[4][1]=int(raw_input(Helix[4][0][:-1]+"["+str(Helix[4][1])+"]: "))#initSeqqNo
        Helix[2][1]=oneTo3[sequence[(int(Helix[4][1])-1)]]#extract sequence name from dictionary
        print "The position corresponds to amino acid",Helix[2][1]
        Helix[8][1]=int(raw_input(Helix[8][0][:-1]+"["+str(Helix[8][1])+"]: "))
        Helix[6][1]=oneTo3[sequence[(int(Helix[8][1])-1)]]
        print "The position corresponds to amino acid",Helix[6][1]
        Helix[12][1]=(Helix[8][1])-(Helix[4][1])
        Helix[10][1]=int(raw_input(Helix[10][0][:-1]+"["+str(Helix[10][1])+"]: "))
        n=Helix[10][1]
        print "The selected class was:",helixClass[n] #work on function to change the class and insert here
        Helix[11][1]=raw_input(Helix[11][0][:-1]+"["+str(Helix[11][1])+"]: ")
        print "The helix", int(response)," has been successfully", action
    return Helix
def editsheet(response,feature,action="edited"):
    if int(response)==int(response): #convert this as a function
        n= int(response)-1
        Sheet= helixSheets[feature][n] #exraxt lists for Helix
        Sheet[4][1]=raw_input(Sheet[4][0]+str(Sheet[4][1])) #chainID
        Sheet[5][1]=int(raw_input(Sheet[5][0][:-1]+"["+str(Sheet[5][1])+"]: "))#initSeqqNo
        Sheet[3][1]=oneTo3[sequence[(int(Sheet[5][1])-1)]]#extract sequence name from dictionary
        print "The position corresponds to amino acid",Sheet[3][1]
        Sheet[9][1]=int(raw_input(Sheet[9][0][:-1]+"["+str(Sheet[9][1])+"]: "))
        Sheet[7][1]=oneTo3[sequence[(int(Sheet[9][1])-1)]]
        print "The position corresponds to amino acid",Sheet[7][1]
##        Sheet[12][1]=(Sheet[8][1])-(Sheet[4][1])
##        Sheet[10][1]=int(raw_input(Sheet[10][0][:-1]+"["+str(Sheet[10][1])+"]: "))
##        n=Sheet[10][1]
##        print "The selected class was:",SheetClass[n] #work on function to change the class and insert here
##        Sheet[11][1]=raw_input(Sheet[11][0][:-1]+"["+str(Sheet[11][1])+"]: ")
        print "The Sheet", int(response)," has been successfully", action
    return Sheet
def confirmS():
    PDBfile.seek(0)
    for line in PDBfile:
        if line.startswith("SHEET") and line[9]==str(n) and (line[13]=="B" or line[13]=="C"):
            return line
def confirmH():
    PDBfile.seek(0)
    for line in PDBfile:
        if line.startswith("HELIX") and line[9]==str(n):
            return line
                    
sequence='YNFFPRKPKWDKNQITYRIIGYTPDLDPETVDDAFARAFQVWSDVTPLRFSRIHDGEADIMINFGRWEHGDGYPFDGKDGLLAHAFAPGTGVGGDSHFDDDELWTLGKGVGYSLFLVAAHAFGHAMGLEHSQDPGALMAPIYTYTKNFRLSQDDIKGIQELYGASPD'
oneTo3={'A': 'ALA', 'C': 'CYS', 'E': 'GLU', 'D': 'ASP', 'G': 'GLY', 'F': 'PHE', 'I': 'ILE', 'H': 'HIS', 'K': 'LYS', 'M': 'MET', 'L': 'LEU', 'N': 'ASN', 'Q': 'GLN', 'P': 'PRO', 'S': 'SER', 'R': 'ARG', 'T': 'THR', 'W': 'TRP', 'V': 'VAL', 'Y': 'TYR'}
print "Choose one of the Manipulation Options:\nList(L) Edit(E) New(N) Remove(R) Main Menu(M)"
response =raw_input(":")
if response.upper()=="E":
    feature=raw_input("Do you want to edit a Helix (H) or a Sheet (S): ")
    while feature!="":
        if feature.upper()=="H":
            feature="Helix"
            response=raw_input("Which Helix do you want to edit 1-"+str(len(helixSheets["Helix"])))
            while response!="":
                Helix=edit(response,feature)
                response=raw_input("Which Helix do you want to edit (1-"+str(len(helixSheets["Helix"])))
                feature=raw_input("Do you want to edit a Helix (H) or a Sheet (S): ")
        elif feature.upper()=="S":
            feature="Sheet"
            response=raw_input("Which Sheet do you want to edit 1-"+str(len(helixSheets["Sheet"])))
            while response!="":
                Sheet=editsheet(response,feature)
                response=raw_input("Which sheet do you want to edit (1-"+str(len(helixSheets["Sheet"]))+"): ")
        else:
            feature=raw_input("Do you want to edit a Helix (H) or a Sheet (S): ")
print "Choose one of the Manipulation Options:"
response=raw_input("List(L) Edit(E) New(N) Remove(R) Main Menu(M")
if response.upper()=="N":
    response=raw_input("Do you want to add a Helix (H) or a Sheet (S): ")
    while response!="":
        if response.upper()=="H":
            n=len(helixSheets["Helix"])+1
            helixSheets["Helix"]+=[[["serNum:",int(n)],["helixID:",int()],
                                  ["initResName:",""],["initChainID:","A"],
                                  ["initSeqNum:",int(1)],["initICode:",None],
                                  ["endResName:",None],["endChainID:",None],
                                  ["endSeqNum:",None],["endICode:",None],
                                  ["helixClass:",int(1)],["comment:",""],
                                  ["length:",int(1)]]]
            response=len(helixSheets["Helix"])
            feature= "Helix"
            Helix=edit(response,feature,"created")
            response=raw_input("Do you want to add a Helix (H) or a Sheet (S): ")
        elif response.upper()=="S":
            helixSheets["Sheet"] +=[[["strand:",None],["sheetID:",None],
                                       ["numStrands",None],["initResName:",None],
                                       ["initChainID:",None],
                                      ["initSeqNum:",int(1)],["initICode:",None],
                                      ["endResName:",None],["endChainID:",None],
                                      ["endSeqNum:",int(1)],["endICode:",None],
                                      ["sense:",None],["curAtom:",None],
                                       ["curResName:",None],["curChainId:",None],
                                    ["curResSeq:",None],["curIcode:",None],
                                      ["prevAtom:",None],["prevResName:",None],
                                       ["prevChainId:",None],["prevResSeq:",None],
                                       ["prevICode:",None]]]
            response=len(helixSheets["Sheet"])
            feature= "Sheet"
            Helix=editsheet(response,feature,"created")
            response=raw_input("Do you want to edit a Helix (H) or a Sheet (S): ")
print "Choose one of the Manipulation Options:"
response=raw_input("List(L) Edit(E) New(N) Remove(R) Main Menu(M")
if response.upper()=="R":
    response=raw_input("Do you want to remove a Helix (H) or a Sheet (S): ")
    while response!="":
        if response.upper()=="H":
            response=raw_input("Which Helix do you want to delete (1-"+str(len(helixSheets["Helix"]))+"): ")
            n=int(response)-1
            a=confirmH()
            while response!="":
                response=raw_input("Are you sure do you want to delete the helix? \n"+str(a)+"\n Y/N? ")
                if response.upper()=="Y":
                    helixSheets["Helix"].remove(helixSheets["Helix"][n])
                    print "Helix",int(n)+1,"successfully removed"
                    print "All serial numbers have been updated"
                    response=raw_input("Which Helix do you want to delete (1-"+str(len(helixSheets["Helix"]))+"): ")
            response=raw_input("Do you want to remove a Helix (H) or a Sheet (S): ")
        elif response.upper() =="S":
            response=raw_input("Which Sheet do you want to delete (1-"+str(len(helixSheets["Sheet"]))+"): ")
            while response!="":
                if int(response)==int(response):
                    n=int(response)-1
                    a=confirmS()
                    print a
                    response=raw_input("Y/N? ")
                    if response.upper()=="Y":
                        helixSheets["Sheet"].remove(helixSheets["Sheet"][n])
                        response=response=raw_input("Which Sheet do you want to delete (1-"+str(len(helixSheets["Sheet"]))+"): ")
            
                    
                           
                                                                       
                                                                           

 

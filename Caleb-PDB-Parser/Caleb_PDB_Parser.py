#PDB Parser
#Caleb Kipkurui Kibet
#g13k8050
import os
import re
import sys
import time
def menu(response):
    '''->None
    Displays the main menu with all the options
    '''
    print "*"*80
    print "%s %60s"%("* PDB FILE ANALYZER","*")
    print "*"*80
    print "%s %49s"%("* Select an option from below:","*")
    print "*%79s"% "*"
    print "*      %s %25s %28s"% ("1) Open a PDB File","(O)","*")
    print "*      %s %28s"%("2) Information                           (I)","*")
    print "*      %s %28s"%("3) Show histogram of amino acids         (H)","*")
    print "*      %s %28s"%("4) Display Secondary Structure           (S)","*")
    print "*      %s %28s"%("5) Manipulate Helix or Sheet             (M)","*")
    print "*      %s %28s"%("6) Export PDB File                       (X)","*")
    print "*      %s %28s"%("7) Exit                                  (Q)","*")
    print "*%79s"%("*")
    print "* %76s *" % ("Current PDB:"+str(response[-8:]))
    print "*"*80
def menu2(response):
    '''->None
    Function displays second menu with only the active options available.
    '''
    print "*"*80
    print "%s %60s"%("* PDB FILE ANALYZER","*")
    print "*"*80
    print "%s %49s"%("* Select an option from below:","*")
    print "*%79s"% "*"
    print "*      %s %25s %28s"% ("1) Open a PDB File","(O)","*")
    print "*%79s"% "*"
    print "*%79s"% "*"
    print "*%79s"% "*"
    print "*%79s"% "*"
    print "*%79s"% "*"
    print "*      %s %28s"%("7) Exit                                  (Q)","*")
    print "*%79s"%("*")
    print "* %76s *" % ("Current PDB:"+str(response))
    print "*"*80

def validatepath():
    '''->File path
    Validates the existence of the path and return the path
    '''
    flag = True
    while flag:
        paths = raw_input("Enter a valid PATH for a PDB file: ")
        if os.path.exists(paths)and os.path.isfile(paths):
          flag = False
    else:
        return paths

def validatePDB(paths):
    '''->File
    Validates if the entered fiel is a valid PDB file and returns it
    '''
    PDBfile=open(paths,"r")
    header = PDBfile.read(6)
    while header!="HEADER":
        paths = validatepath()
        PDBfile=open(paths,"r")
        header = PDBfile.read(6)
    else:
        return PDBfile
def chainLists():
    '''->List
    Identifies and lists chain in the PDB file
    '''
    chains =[]
    PDBfile.seek(0)
    for line in PDBfile:
        if line.startswith("SEQRES"):
            if line[11] not in chains:
                chains+=line[11]
    return chains
def optionO(currentPDB):
    '''->tuple
    tuple to store PDBfile and current PDB
    '''
    var=()
    currentPDB = validatepath()
    PDBfile=validatePDB(currentPDB)
    print "The File %s has been successfully loaded" %currentPDB[-8:]
    var=(currentPDB,PDBfile)
    return var

#######################################INFORMATION DSPLAY######################################################################            
def add_to_PDBdict(PDB,key,seq):
    '''->dict
    Funtion that adds data to a dictionary PDB
    '''
    PDB[key]=seq
    return PDB

def extractTitle(PDBfile):
    '''->str
    Extracts the title of the PDB file and returns
    a string of TITLE
    '''
    PDBfile.seek(0)
    title = "Title: "
    for line in PDBfile:
        if line.startswith("TITLE"):
            title += line[10:80].rstrip()
    return title
def extractSeq(PDBfile,char):
    '''->str
    extracts the sequence from the PDB file and returns a
    string of sequences.
    '''
    PDBfile.seek(0)
    seq=""
    for line in PDBfile:
        if line.startswith("SEQRES")and line[11]==char:
            seq+=line[18:70]
    return seq
def oneto3(seq,dict):
    '''->str
    Converts the three letter amino acids to the single letter version
    and returns a string of sequences
    '''
    oneaa = ""
    for i in seq:
        if i !="":
            oneaa+=dict[i]
    return oneaa
def parseSequence(sequence,numberperline,indentation=0):
    '''->str
    Formats the sequences to a specific lenght and returns a string of
    formatted sequence
    '''
    seq=""
    index=0
    while index<len(sequence):
        if index==0:
            seq =sequence[index:index+numberperline] + "\n"
            index +=numberperline
        else:
            seq += " "*indentation +sequence[index:index+numberperline] + "\n"
            index +=numberperline
    return seq
def ectractSheetInfo():
    '''->list
    Extracts sheet information for the PDB file and returns a
    list containig the information
    '''    
    PDBfile.seek(0)
    sheetLists =[]
    for line in PDBfile:
        if line.startswith("SHEET"):
            sheetLists +=[[["strand:",line[8:10].strip()],["sheetID:",line[12:14].strip()],
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
    return sheetLists
def extractHelixInfo():
    '''->list
    Extracts helix information for the PDB file and returns a
    list containig the information
    '''
    PDBfile.seek(0)
    helixLists =[]
    for line in PDBfile:
        if line.startswith("HELIX"):
            helixLists +=[[["serNum:",int(line[7:10].strip())],["helixID:",int(line[11:14].strip())],
                      ["initResName:",line[15:18].strip()],["initChainID:",line[19:20].strip()],
                      ["initSeqNum:",int(line[22:25].strip())],["initICode:",line[25:26].strip()],
                      ["endResName:",line[27:30].strip()],["endChainID:",line[31:32].strip()],
                      ["endSeqNum:",int(line[34:37].strip())],["endICode:",line[37:38].strip()],
                      ["helixClass:",int(line[39:40].strip())],["comment:",line[41:70].strip()],
                      ["length:",int(line[72:76].strip())]],]
    return helixLists

def optionI():
    '''->None
    Function displays a summary of information on the PDB file
    '''
    print "PDB file: %s"% currentPDB[-8:]
    title = extractTitle(PDBfile)
    seq= parseSequence(title,80).rstrip()
    print seq
    print "CHAINS: ",
    for i in range(len(chainList)):
        if len(chainList)== 2:
            if i==len(chainList)-1:
                print "and", chainList[i]
            else:
                print chainList[i],
        else:
            if i==len(chainList)-1:
                print "and", chainList[i]
            else:
                print chainList[i],",",
    for i in chainList:
        print " - chain",i
        seq= extractSeq(PDBfile,i)
        seq = oneto3(seq.split(" "),threeTO1)
        print "   Number of Amino acids:%4s"% len(seq)
        print "   Number of helix:%10s"% countFeature(PDBfile,i,31,"HELIX")
        print "   Number of sheet:%10s"% countFeature(PDBfile,i,32,"SHEET")
        print "   Sequence:  ",parseSequence(seq,50,15)
        
def PDBDict():
    '''->dict
    Function to extract PDB file sequence and title information,
    stores in  a dictionary
    '''
    title = extractTitle(PDBfile)
    seq= parseSequence(title,80).rstrip()
    PDB ={}
    PDB =add_to_PDBdict(PDB,"Title",seq)
    for i in chainList:
        PDB =add_to_PDBdict(PDB,"Title",seq)
        seq= extractSeq(PDBfile,i)
        PDB =add_to_PDBdict(PDB,("ThreeSeq%s"% i),seq.rstrip())
        seq = oneto3(seq.split(" "),threeTO1)
        PDB =add_to_PDBdict(PDB,("Sequence%s" % i),seq)
    return PDB
##############################################HISTOGRAM OF AMINO ACIDS###################################################################
def sort_by(seq,i,sort):
        seq = sorted(seq, key=lambda x: x[i], reverse = sort)            
        for i in seq:
            if i[1] !=0:
                print "%s (%3i) : %s"% (i[0],i[1],"*"*i[1])
def optionH():
    '''->None
    Funtion to draw a histogram summarising the distribution
    of amino acids in the protein
    '''
    print '''Choose an option to order by or [enter] to exit: 
      number of amino acids - ascending  (an)
      number of amino acids - descending (dn)
      alphabetically - ascending         (aa)
      alphabetically - descending        (da)'''
    count_of_aa=[]
    List_of_aa= ["Ala","Arg","Asn","Asp","Asx","Cys","Gln","Glu","Glx","Gly","His",
          "Ile","Leu","Lys","Met","Phe","Pro","Ser","Thr","Trp","Tyr","Val"]
    sequence = PDB['ThreeSeqA']+PDB['ThreeSeqB']
    for i in List_of_aa:
        count=sequence.count(i.upper())
        count_of_aa+=[(i,count)] # list of tuple to store count of aa
    response =raw_input("order by: ")
    while response !="":
        if response.lower() == "an":
            sort_by(count_of_aa,0,False)
            response =raw_input("order by: ")
        if response.lower() == "dn":
            sort_by(count_of_aa,0,True)
            response =raw_input("order by: ")
        if response.lower() == "aa":
            sort_by(count_of_aa,1,False)
            response =raw_input("order by: ")
        if response.lower() == "da":
            sort_by(count_of_aa,0,True)
            response =raw_input("order by: ")

#################################################DISPLAY SECONDARY STRUCTURE##################################################################

def extractSructure(j):
    '''->dict
    Extracts helix and sheet sec structure information
    '''
    chain = {}
    Helix =[]
    Sheet = []
    for i in helixSheets["Helix"]:
        if i[3][1]==j:
            Helix += [[str(i[1][1]),i[4][1],i[8][1]]]
    for i in helixSheets["Sheet"]:
        if i[4][1]==j:        
            Sheet += [[str(i[0][1])+str(i[1][1]),i[5][1],i[9][1]]]
        chain["Helix%s"% j]=Helix
        chain["Sheet%s"% j]=Sheet
    return chain
def parselen(string,noperline,indentation=0):
    seq = ()
    i = 0
    while i <len(string):
        seq+= (" "*indentation+string[i:i+noperline]+"\n",)
        i += noperline
    return seq
def chain(Chain,Helix,Sheet,seq):
    '''Formats and prints out the secondary structure by 
    '''
    s = "|"
    h = "/"
    helix =[]
    sheet =[]
    secStructure = ""
    tagid = ""
    taglist=[' ']*len(seq)
    structure=["-"]*len(seq)
    if Sheet in Chain.keys():
        for i in Chain[Sheet]:
            a=(i[1]-1)
            b=i[2]
            structure[a:b] = s*((b-a))
        for i in Chain[Sheet]:
            a=(i[1]-1)
            b=i[2]
            n=len(i[0])
            taglist[a:a+n] = i[0]
    if Helix in Chain.keys():
        for i in Chain[Helix]:
            a=(i[1]-1)
            b=i[2]
            structure[a:b] = h*((b-a))
        for i in Chain[Helix]:
            a=(i[1]-1)
            n=len(i[0])
            taglist[a:a+n] = i[0]
    for i in structure:
        secStructure += i.strip()
    for i in taglist:
        tagid += i
    labels =parselen(tagid,80,indentation=0)
    structure=parselen(secStructure,80,indentation=0)
    sequences=parselen(seq,80,indentation=0)
    for i, j, k in zip(sequences,structure,labels):
        print i,j,k

def Sequence():
    '''->str
    Fuction extracts single letter sequence from the PDB file
    '''
    for i in chainList:
        Sequence=""
        Sequence +=PDB["Sequence%s"% i]
        return Sequence
def optionS():
    '''->None
    Draws the secondary srtucture of the protein
    '''
    print "Secondary structure of the PDB id %s " % currentPDB[:4] 
    for i in chainList:
        print "Chain%s"% i
        print "(1)"
        ChainA=extractSructure(i)
        SequenceB =PDB["Sequence%s"% i]
        chain(ChainA,("Helix%s"%i),("Sheet%s"% i),SequenceB)
        print "(%s)" %len(SequenceB)
        print
        

#####################################MANIPULATE HELIX OR SHEET###########################################################
def DisplayH(n):
    '''->dict
    For displaying the helix to be removed
    '''
    h=helixSheets["Helix"][n-1]
    helix = "HELIX %4s %3s %3s %s %4s %s %s %2s %3s %s %s %32s %2s"%(str(h[0][1]),str(h[1][1]),
                            str(h[2][1]),str(h[3][1]),str(h[4][1]),str(h[5][1]),str(h[6][1]),str(h[7][1]),
                            str(h[8][1]),str(h[9][1]),str(h[10][1]),str(h[11][1]),str(h[12][1]))
    return helix
def DisplayS(m):
    '''->dict
    For displaying the sheet to be removed
    '''
    s=helixSheets["Sheet"][m-1]
    helixSheets["Sheet"][m-1]
    sheet = "SHEET %4s %3s %1s %1s %1s %3s %s %s %s %3s %s %s %2s  %s %s %3s %s %2s %4s %s %3s %s"%(str(s[0][1]),
    str(s[1][1]),str(s[2][1]),str(s[3][1]),str(s[4][1]),str(s[5][1]),str(s[6][1]),str(s[7][1]),str(s[8][1]),str(s[9][1]),
    str(s[10][1]),str(s[11][1]),str(s[12][1]),str(s[13][1]),str(s[14][1]),str(s[15][1]),str(s[16][1]),str(s[17][1]),
    str(s[18][1]),str(s[19][1]),str(s[20][1]),str(s[21][1]))
    return sheet
    
def countFeature(PDBfile,char,n,feature):
    '''->int
    Fuction counts the number of sheets or helices in the PDB fil
    and returns the count
    '''
    PDBfile.seek(0)
    count = 0
    for line in PDBfile:
        if line.startswith(feature)and line[n]==char: 
            count+=1
    return count
def editHelix(response,feature,action="edited"):
    '''->dict
    Edits the helix and returns the edited helix for
    use in optionE
    '''
    if response!="":
        n= int(response)-1
        Helix= helixSheets[feature][n] #exraxt lists for Helix
        Helix[3][1]=raw_input(Helix[3][0]+"["+str(Helix[3][1])+"]: ") #chainID
        Helix[4][1]=int(raw_input(Helix[4][0][:-1]+"["+str(Helix[4][1])+"]: "))#initSeqqNo
        Helix[2][1]=oneTo3[sequence[(int(Helix[4][1])-1)]]#extract sequence name from dictionary
        print "The position corresponds to amino acid",Helix[2][1]
        Helix[8][1]=int(raw_input(Helix[8][0][:-1]+"["+str(Helix[8][1])+"]: "))
        Helix[6][1]=oneTo3[sequence[(int(Helix[8][1])-1)]]
        print "The position corresponds to amino acid",Helix[6][1]
        Helix[12][1]=(Helix[8][1])-(Helix[4][1])
        Helix[10][1]=int(raw_input(Helix[10][0][:-1]+"["+str(Helix[10][1])+"]: "))
        n=Helix[10][1]
        print "The selected class was:",helixClass[n]
        Helix[11][1]=raw_input(Helix[11][0][:-1]+"["+str(Helix[11][1])+"]: ")
        print "The helix", int(response)," has been successfully", action
        return Helix
def editSheet(response,feature,action="edited"):
    '''->dict
    Edits the sheet and returns the edited sheet for
    use in optionE
    '''
    if response!="": 
        n= int(response)-1
        Sheet= helixSheets[feature][n] #exract lists for Helix 
        Sheet[4][1]=raw_input(Sheet[4][0]+"["+str(Sheet[4][1])+"]: ") 
        Sheet[5][1]=int(raw_input(Sheet[5][0][:-1]+"["+str(Sheet[5][1])+"]: "))#initSeqqNo
        Sheet[3][1]=oneTo3[sequence[(int(Sheet[5][1])-1)]]#extract sequence name from dictionary
        print "The position corresponds to amino acid",Sheet[3][1]
        Sheet[9][1]=int(raw_input(Sheet[9][0][:-1]+"["+str(Sheet[9][1])+"]: "))
        Sheet[7][1]=oneTo3[sequence[(int(Sheet[9][1])-1)]]
        print "The position corresponds to amino acid",Sheet[7][1]
        print "The Sheet", int(response)," has been successfully", action
        return Sheet
def creatSheet(response,feature,action="edited"):
    '''->dict
    Edits the sheet and returns the edited sheet for
    use in optionN
    '''
    if response!="": 
        n= int(response)-1
        Sheet= helixSheets[feature][n]
        #Sheet[4][1]=raw_input(Sheet[4][0]+"["+str(Sheet[4][1])+"]: ") 
        Sheet[5][1]=int(raw_input(Sheet[5][0][:-1]+"["+str(Sheet[5][1])+"]: "))#initSeqqNo
        Sheet[3][1]=oneTo3[sequence[(int(Sheet[5][1])-1)]]#extract sequence name from dictionary
        print "The position corresponds to amino acid",Sheet[3][1]
        Sheet[9][1]=int(raw_input(Sheet[9][0][:-1]+"["+str(Sheet[9][1])+"]: "))
        Sheet[7][1]=oneTo3[sequence[(int(Sheet[9][1])-1)]]
        print "The position corresponds to amino acid",Sheet[7][1]
        print "The Sheet", int(response)," has been successfully", action
        return Sheet

def SheetToEdit():
    '''->None
    Displays the serial numbers of the sheets to be reomved or
    edited and corresponding choic to perform the action
    '''
    dict={}
    n=9
    for i in range(len(helixSheets["Sheet"])):
        dict[i+1]=str(helixSheets["Sheet"][i][0][1])+str(helixSheets["Sheet"][i][1][1])
    for key in dict:
        if int(key)==n:
            print
            print key,"->",dict[key],
            n+=9
        elif key==len(dict):
            print key,"->",dict[key],
            print
        else:
            print key,"->",dict[key],

def optionL():
    '''->None
    Lists the information pertaining to helix or sheet
    '''
    response ="L"
    while response!="":
        response =raw_input("Do you want to list the Helix (H) or the Sheet (S),[enter] for previous menu: ")
        if response.upper() == "S":
            n = 1
            l=len(sheetLists)
            for i in sheetLists:
                print "Sheet "+str(n)+" of "+str(l)+":"
                for j in i:
                    print "  %-13s %s"% (j[0],str(j[1]).strip())
                n +=1
        elif response.upper() == "H":
            n = 1
            l=len(helixLists)
            for i in range(len(helixLists)):
                print "Helix "+str(n)+" of "+str(l)+":"
                for j in helixLists[i]:
                    if j[0] =="helixClass:":
                        print "  %-13s %s"% (j[0],helixClass[int(j[1])])
                    else:
                        print "  %-13s %s"% (j[0],str(j[1]).strip())
                n +=1
    else:
        print "Choose one of the Manipulation Options\nList(L) Edit(E) New(N) Remove(R) Main Menu(M)"

def optionE():
    '''-dict
    Edits the helix and or sheets and returns the updated
    dictionary of of helix and sheets(helixSheets)
    '''
    feature="E"
    while feature!="":
        feature=raw_input("Do you want to edit a Helix (H) or a Sheet (S) [enter] for previous menu: ")
        if feature.upper()=="H":
            feature="Helix"
            response="S"
            while response!="":
                response=raw_input("Which Helix do you want to edit (1-"+str(len(helixSheets["Helix"]))+"): ")
                Helix=editHelix(response,feature)
        if feature.upper()=="S":
            feature="Sheet"
            response="S"
            while response!="":
                SheetToEdit()
                response=raw_input("Which Sheet do you want to edit (1-"+str(len(helixSheets["Sheet"]))+"): ")
                Sheet=editSheet(response,feature)
    else:
        print "Choose one of the Manipulation Options"
        return helixSheets
   
def Increment():
    Alpha=""
    for i in range(len(chainList)):
        if i==len(chainList)-1:
            Alpha=chr(ord(chainList[i]) + 1)
    return Alpha
def optionN():
    '''->dict
    Creates a new helix or sheetreturns the
    updated dictionary of helix and sheets(helixSheets)
    '''
    response="N"
    while response!="":
        response=raw_input("Do you want to add a Helix (H) or a Sheet (S)[enter] for previous menu: ")
        if response.upper()=="H":
            n=len(helixSheets["Helix"])+1
            helixSheets["Helix"]+=[[["serNum:",int(n)],["helixID:",int(n)],
            ["initResName:",""],["initChainID:","A"],["initSeqNum:",int(1)],["initICode:",""],
            ["endResName:",""],["endChainID:",""],["endSeqNum:",""],["endICode:",""],
            ["helixClass:",int(1)],["comment:",""],["length:",int(1)]]]
            response=len(helixSheets["Helix"])
            feature= "Helix"
            Helix=editHelix(response,feature,"created")
        elif response.upper()=="S":
            helixSheets["Sheet"] +=[[["strand:","1"],["sheetID:",str(Increment())],
            ["numStrands","1"],["initResName:",""],["initChainID:",str(Increment())],["initSeqNum:",int(1)],["initICode:",""],
            ["endResName:",""],["endChainID:",str(Increment())],["endSeqNum:",int(1)],["endICode:",""],["sense:","1"],["curAtom:",""],
            ["curResName:",""],["curChainId:",""],["curResSeq:",""],["curIcode:",""],
            ["prevAtom:",""],["prevResName:",""],["prevChainId:",""],["prevResSeq:",""],["prevICode:",""]]]
            response=len(helixSheets["Sheet"])
            feature= "Sheet"
            Sheet=creatSheet(response,feature,"created")
    else:
        print "Choose one of the Manipulation Options:\nList(L) Edit(E) New(N) Remove(R) Main Menu(M)"
        return helixSheets
         
def optionR():
    '''->dict
    Removes helix or sheet from the PDB file and returns the
    updated dictionary of helix and sheets(helixSheets)
    '''
    response="R"
    while response!="":
        response=raw_input("Do you want to remove a Helix (H) or a Sheet (S) [enter] for previous menu: ")
        if response.upper()=="H":
            response="H"
            while response!="":
                response=raw_input("Which helix do you want to delete (1-"+str(len(helixSheets["Helix"]))+"): ")
                if response!="":
                    n=int(response)-1
                    a=DisplayH(n+1)
                    response=raw_input("Are you sure do you want to delete the helix? \n"+str(a)+"\n Y/N? ")
                    if response.upper()=="Y":
                        helixSheets["Helix"].remove(helixSheets["Helix"][n])
                        print "Helix",int(n)+1,"successfully removed"
                        print "All serial numbers have been updated"
        elif response.upper() =="S":
            response="S"
            while response!="":
                SheetToEdit()
                response=raw_input("Which Sheet do you want to delete (1-"+str(len(helixSheets["Sheet"]))+"): ")
                if response!="":
                    n=int(response)-1
                    a=DisplayS(n+1)
                    response=raw_input("Are you sure do you want to delete the sheet? \n"+str(a)+"\n Y/N? ")
                    if response.upper()=="Y":
                        helixSheets["Sheet"].remove(helixSheets["Sheet"][n])
                        print "Sheet",int(n)+1,"successfully removed"
                        print "All serial numbers have been updated"
    else:
        print "Choose one of the Manipulation Options"
        return helixSheets
def UpdateSerialS():
    '''->dic
    Function that Updtes the serial numbers when a sheet
    is deleted
    '''
    for i in chainList:
        n=0
        for j in helixSheets["Sheet"]: 
            if j[1][1]==i:
                n+=1
                j[0][1]=n
        for j in helixSheets["Sheet"]:
            if j[1][1]==i:
                j[2][1]=n
    return helixSheets
def updateSerialH():
    '''->dict
    Function that Updtes the serial numbers when a sheet
    is deleted
    '''
    n=1
    for i in range(len(helixSheets["Helix"])):
        h=helixSheets["Helix"][i]
        h[0][1]=n
        h[1][1]=n
        n+=1
    return helixSheets
def writeToFile():
    '''->file
    writes a new PDB file form the old one replacing
    the edited the new and edited helix and or sheet
    and adding current date to the header and updating unique ID
    '''
    PDBfile.seek(0)
    flag=True
    while flag:
        path = raw_input("Filepath(4 letter alphanmeric): ").upper()+".pdb"
        new = open(path, "w")
        if os.path.exists:
            ask = raw_input("Do you want to overwrite the file "+path+"?(Y/N) ")
            if ask.upper()=="Y":
                flag=False
            else:
                flag=True
    for line in PDBfile:
        if line.startswith("HEADER"):
            line = line[0:50]+time.strftime("%d/%m/%Y")+line[60:62]+str(path[:4])+"\n"
            new.write(line)
        elif line.startswith("DBREF"):
            line=line[:7]+str(path[:4])+line[11:]
            new.write(line)
        elif line.startswith("SEQADV"):
            line=line[:7]+str(path[:4])+line[11:]
            new.write(line)
        elif line.startswith("HELIX") and line[7:10].strip()==str(1):
            for i in range(len(helixSheets["Helix"])):
                h=helixSheets["Helix"][i]
                line = "HELIX %4s %3s %3s %s %4s %s %s %2s %3s %s %s %-32s %2s \n"%(str(h[0][1]),str(h[1][1]),
                        str(h[2][1]),str(h[3][1]),str(h[4][1]),str(h[5][1]),str(h[6][1]),str(h[7][1]),
                        str(h[8][1]),str(h[9][1]),str(h[10][1]),str(h[11][1]),str(h[12][1]))
                new.write(line)
        elif line.startswith("HELIX"):
            continue
        elif line.startswith("SHEET") and line[9]==str(1) and line[13]=="A":
            for i in range(len(helixSheets["Sheet"])):
                s=helixSheets["Sheet"][i]
                line = "SHEET %4s %3s %1s %1s %1s %3s %s %s %s %3s %s %s %2s  %s %s %3s %s %2s %4s %s %3s %s \n"%(str(s[0][1]),
                str(s[1][1]),str(s[2][1]),str(s[3][1]),str(s[4][1]),str(s[5][1]),str(s[6][1]),str(s[7][1]),str(s[8][1]),str(s[9][1]),
                str(s[10][1]),str(s[11][1]),str(s[12][1]),str(s[13][1]),str(s[14][1]),str(s[15][1]),str(s[16][1]),str(s[17][1]),
                str(s[18][1]),str(s[19][1]),str(s[20][1]),str(s[21][1]))
                new.write(line)
        elif line.startswith("SHEET"):
            continue
        else:
            line=line
            new.write(line)

##################################################CORE MAIN PROGRAM######################################################################
currentPDB = None
choices = ("M","O","I","H","S","X","Q")
response="Q"
while response.upper() in choices:
    if currentPDB==None:
        menu2(currentPDB)
        response = raw_input(":")
    else:
        menu(currentPDB)
        response = raw_input(":")
    if response.upper() in choices:
        if response.upper() =="O":
            if currentPDB==None:
                var=optionO(currentPDB)
                PDBfile=var[1]
                currentPDB=var[0]
            else:
                ans =raw_input("Do you want to replace (y/n)" )
                if ans.lower()=="y":
                    var=optionO(currentPDB)
                else:
                    PDBfile=var[1]
                    currentPDB=var[0]
            PDBfile=var[1]
            currentPDB=var[0]
            chainList=chainLists()#stores the chains in PDB file
            chainList.sort()
            helixSheets ={}#Dictionary of lists that stores all data
            helixLists=extractHelixInfo()
            sheetLists=ectractSheetInfo()
            helixSheets["Helix"]=helixLists
            helixSheets["Sheet"]=sheetLists
            threeTO1 ={'VAL':'V', 'ILE':'I', 'LEU':'L', 'GLU':'E', 'GLN':'Q',
                     'ASP':'D', 'ASN':'N', 'HIS':'H', 'TRP':'W', 'PHE':'F', 'TYR':'Y',
                    'ARG':'R', 'LYS':'K', 'SER':'S', 'THR':'T', 'MET':'M', 'ALA':'A',
                    'GLY':'G', 'PRO':'P', 'CYS':'C'}
            oneTo3={'A': 'ALA', 'C': 'CYS', 'E': 'GLU', 'D': 'ASP', 'G': 'GLY', 'F': 'PHE', 'I': 'ILE', 'H': 'HIS',
                'K': 'LYS', 'M': 'MET', 'L': 'LEU', 'N': 'ASN', 'Q': 'GLN', 'P': 'PRO', 'S': 'SER', 'R': 'ARG',
                'T': 'THR', 'W': 'TRP', 'V': 'VAL', 'Y': 'TYR'}
            helixClass={1:"Right-handed alpha",2:"Right-handed omega",3:"Right-handed pi",4:"Right-handed gamma",
                    5:"Right-handed 3 - 10",6:"Left-handed alpha",7:"Left-handed omega",8:"Left-handed gamma",
                    9:"2 - 7 ribbon/helix",10:"Polyproline"}
            PDB=PDBDict()#stores the chains sequences data in a dictionary
            sequence = Sequence()
        if response.upper() == "I":
            optionI()
        if response.upper() =="H":
            optionH()
        if response.upper() == "S":
            helixSheets=updateSerialH()
            helixSheets=UpdateSerialS()
            optionS()
        if response.upper()=="M":
            print "Choose one of the Manipulation Options \n List(L)  Edit(E)  New(N)  Remove(R)  Main Menu(M)"
            entry = raw_input(":")
            while entry!="":
                if entry.upper() == "L":
                    optionL()
                    entry =raw_input(":")
                elif entry.upper()=="E":
                    helixSheets=optionE()
                    entry=raw_input("List(L) Edit(E) New(N) Remove(R) Main Menu(M): ")
                elif entry.upper()=="N":
                    helixSheets=optionN()
                    #chainList+=[Increment()]
                    entry =raw_input(":")
                elif entry.upper()=="R":
                    helixSheets=optionR()
                    entry = raw_input("List(L) Edit(E) New(N) Remove(R) Main Menu(M):  ")
                else:
                    entry=""
        if response.upper()=="X":
            helixSheets=updateSerialH()
            helixSheets=UpdateSerialS()
            entry=response
            while entry!="":
                writeToFile()   
                print "FILE SAVED"
                entry=raw_input("Press [enter] to go back to the menu")

        if response.upper()=="Q":
            flag = True
            response=raw_input("Do you want to exit (E) or do you want to go back to menu (M): ")
            if response.upper()=="E":
                print
                os._exit(1)
    else:
        print "Error invalid choice"
        response="Q"
##################################################END OF PROGRAM#####################################################
#                   Thank you so much for Helping Me understand Python                                              #
#####################################################################################################################

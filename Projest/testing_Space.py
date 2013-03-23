
    response=raw_input("Which Helix do you want to edit (1-3): ")
def edit(response,feature)
    if int(response)==1: #convert this as a function
        n= response-1
        Helix= helixSheets["Helix"][n] #exraxt lists for Helix
        Helix[3][1]=raw_input(Helix[3][0]+str(Helix[3][1])) #chainID
        Helix[4][1]=int(raw_input(Helix[4][0][:-1]+"["+str(Helix[4][1])+"]: "))#initSeqqNo
        Helix[2][1]=oneTo3[sequence[(int(Helix[4][1])-1)]]#extract sequence name from dictionary
        print "The position corresponds to amino acid",Helix[2][1]
        Helix[8][1]=int(raw_input(Helix[8][0][:-1]+"["+str(Helix[8][1])+"]: "))
        Helix[6][1]=oneTo3[sequence[(int(Helix[8][1])-1)]]
        print "The position corresponds to amino acid",Helix[6][1]
        Helix[12][1]=(Helix[8][1])-(Helix[4][1])
        Helix[10][1]=int(raw_input(Helix[10][0][:-1]+"["+str(Helix[10][1])+"]: "))
        print "The selected class was:" #work on function to change the class and insert here
        Helix[11][1]=raw_input(Helix[11][0][:-1]+"["+str(Helix[11][1])+"]: ")
        print "The helix", response," has been successfully edited"
    return Helix
def create(response,feature):
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
        print "The selected class was:" #work on function to change the class and insert here
        Helix[11][1]=raw_input(Helix[11][0][:-1]+"["+str(Helix[11][1])+"]: ")
        print "The helix", int(response)," has been successfully edited"
    return Helix

helixSheets["Helix"]+=[["serNum:",int(raw_input("serNum:"))],["helixID:",int(raw_input("helixID:"))],
                      ["initResName:",raw_input("initResName:")],["initChainID:",raw_input("initChainID:")],
                      ["initSeqNum:",int(raw_input("initSeqNum:"))],["initICode:",raw_input("initICode:")],
                      ["endResName:",raw_input("endResName:")],["endChainID:",raw_input("endChainID:")],
                      ["endSeqNum:",int(raw_input("endSeqNum:"))],["endICode:",raw_input("endICode:")],
                      ["helixClass:",int(raw_input("helixClass:"))],["comment:",raw_input("comment:")],
                      ["length:",int(("length:"))]]
helixSheets["Helix"]+=[["serNum:",int(raw_input("serNum:"))],["helixID:",int(raw_input("helixID:"))],
                          ["initResName:",raw_input("initResName:")],["initChainID:",raw_input("initChainID:")],
                          ["initSeqNum:",int(raw_input("initSeqNum:"))],["initICode:",raw_input("initICode:")],
                          ["endResName:",raw_input("endResName:")],["endChainID:",raw_input("endChainID:")],
                          ["endSeqNum:",int(raw_input("endSeqNum:"))],["endICode:",raw_input("endICode:")],
                          ["helixClass:",int(raw_input("helixClass:"))],["comment:",raw_input("comment:")],
                          ["length:",int(("length:"))]]


helixClass={1:"Right-handed alpha",2:"Right-handed omega",3:"Right-handed pi",4:"Right-handed gamma",
            5:"Right-handed 3 - 10",6:"Left-handed alpha",7:"Left-handed omega",8,"Left-handed gamma",
            9:"2 - 7 ribbon/helix",10:"Polyproline"}

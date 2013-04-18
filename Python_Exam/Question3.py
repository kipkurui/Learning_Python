interactions={}
proteins=None
while proteins !="":
    proteins=raw_input("input an interaction: ")
    if proteins!="":
        if "," not in proteins:
            print "ERROR: The inputted text is not in correct format: P1,P2"
            proteins=raw_input("input an interaction: ")
        else:
            proteins=proteins.split(",")
            if proteins[0] in interactions:
                interactions[proteins[0]]+=[proteins[1]]
            else:
                interactions[proteins[0]]=[proteins[1]]
            if proteins[1] in interactions:
                interactions[proteins[1]]+=[proteins[0]]
            else:
                interactions[proteins[1]]=[proteins[0]]
        proteins=raw_input("input an interaction: ")
query=raw_input("Which protein do you want to query? ")
while query !="":
    if query not in interactions:
        print "Protein",query,"doesnt have an interaction regestered in the system."
        query=raw_input("Which protein do you want to query? ")
    else:
        print "The interactions with",query,"are: "
        for i in interactions[query]:
            print i
        query=raw_input("Which protein do you want to query? ")


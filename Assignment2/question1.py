nucleotides = [
	"tttacgatcgatgtATCATTgtgatcgtagcgatgtatTATggcggcc",
	"tttgggta",
	"tgactgtagcagtcaTATCGATG",
	"TTTTTGGTTGTGTGCAAGCTCGGCAGACTTt",
	"ACTGATCGTCGATGCATGTCAGTAGCTAGCCATGTCAGTCAT"]
count =()
lists = []
T = 0
C = 0
A = 0
G = 0
for i in range(len(nucleotides)):
    T = 0
    C = 0
    A = 0
    G = 0
    T =T + nucleotides[i].lower().count('t')
    C =C + nucleotides[i].lower().count('c')
    A =A + nucleotides[i].lower().count('a')
    G =G + nucleotides[i].lower().count('g')
    count = (A,T,G,C)
    lists = lists + [count]
##for i in nucleotides:
##    C =C + i.lower().count('c')
##count = count + (C,)
##for i in nucleotides:
##    A =A + i.lower().count('a')
##count = count +(A,)
##for i in nucleotides:
##    G =G + i.lower().count('g')
##count = count + (G,)
##
##print count

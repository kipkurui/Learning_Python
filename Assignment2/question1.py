nucleotides = [
	"tttacgatcgatgtATCATTgtgatcgtagcgatgtatTATggcggcc",
	"tttgggta",
	"tgactgtagcagtcaTATCGATG",
	"TTTTTGGTTGTGTGCAAGCTCGGCAGACTTt",
	"ACTGATCGTCGATGCATGTCAGTAGCTAGCCATGTCAGTCAT"]
def count(nucleotides):
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
    return lists

print count(nucleotides)

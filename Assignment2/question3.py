nucleotides = [
	"tttacgatcgatgtATCATTgtgatcgtagcgatgtatTATggcggcc",
	"tttgggta",
	"tgactgtagcagtcaTATCGATG",
	"TTTTTGGTTGTGTGCAAGCTCGGCAGACTTt",
	"ACTGATCGTCGATGCATGTCAGTAGCTAGCCATGTCAGTCAT"]
nucleotides = [raw_input("Enter sequences, blank to stop: " )]
if nucleotides!="":
    sequences = nucleotides
while nucleotides != "":
    nucleotides = raw_input("Enter sequences, blank to stop: " )
    if nucleotides!="":
        sequences = sequences + [nucleotides] 


count =()
lists = []
for i in range(len(sequences)):
    T = 0
    C = 0
    A = 0
    G = 0
    N = 0
    T =T + sequences[i].lower().count('t')
    C =C + sequences[i].lower().count('c')
    A =A + sequences[i].lower().count('a')
    G =G + sequences[i].lower().count('g')
    N = len(sequences[i])-(T+C+G+A)
    count = (A,T,G,C,N)
    lists = lists + [count]
print lists
##Question three, formatting display
nuc = ("A","T","G","C","*")
n = 1
nucdict = {}
for i in range(len(sequences)):
    nucdict['SEQUENCE'+ str(i+1)]=sequences[i]  
for i in range(len(lists)):
    print 'SEQUENCE'+str(n) ,":" ,nucdict['SEQUENCE'+str(n)]
    n +=1
    for j,k in zip(nuc,lists[i]):
        print j,"|",k
        print"-------"

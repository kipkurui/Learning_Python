def input_seq():
    nucleotides = [raw_input("Enter sequences, blank to stop: " )]
    if nucleotides!="":
        sequences = nucleotides
    while nucleotides != "":
        nucleotides = raw_input("Enter sequences, blank to stop: " )
        if nucleotides!="":
            sequences = sequences + [nucleotides]
    return sequences

def count(sequences):
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
    return lists
def GC_ratio(lists):
    gcrat = []
    for i in (lists):
        ratio = float(i[2]+i[3])/(i[0]+i[1]+i[2]+i[3]+i[4])
        gcrat = gcrat + [ratio]
    return gcrat

def replace(lists):
    nucs = []
    for i in lists:
        i=i.replace('c','C')
        i=i.replace('g','G')
        i=i.replace('T','t')
        i=i.replace('A','a')
        nucs = nucs + [i]
    return nucs

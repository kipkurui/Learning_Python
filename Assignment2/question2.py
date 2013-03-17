def input_seq():
    nucleotides = [raw_input("Enter sequences, blank to stop: " )]
    if nucleotides!="":
        sequences = nucleotides
    while nucleotides != "":
        nucleotides = raw_input("Enter sequences, blank to stop: " )
        if nucleotides!="":
            sequences = sequences + [nucleotides]
    return sequences
sequences = input_seq()
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
print count(sequences)

        

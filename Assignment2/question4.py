'''(60%)Create a program that receive as many sequences as the user wants
and calculates the GC ratio of each sequence. It should displays the
sequences in order of its GC ratio, with the G's and C's in upper case
and the T's and A's in lower case and in front of the sequence the
calculated GC ratio.Finally it should show was the avarage GC ration
among all the sequences.'''

##from question2 import input_seq
##from question2 import count
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

def input_seq():
    nucleotides = [raw_input("Enter sequences, blank to stop: " )]
    if nucleotides!="":
        sequences = nucleotides
    while nucleotides != "":
        nucleotides = raw_input("Enter sequences, blank to stop: " )
        if nucleotides!="":
            sequences = sequences + [nucleotides]
    return sequences

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

sequences = input_seq()
nuccount = count(sequences)
gcrat = GC_ratio(nuccount)
dispnuc = replace(sequences)
dic = {}
keys = []
for i,j in zip(dispnuc,gcrat):
    dic[j] = i
for key in dic:
    keys=keys+[key]
keys = sorted(keys, key=float)
for i in range(len(keys)):
    print "%40s \t : %5.3f " %(dic[keys[i]],keys[i])
print "The avarage GC content is %5.3f:"% (sum(keys)/len(keys))
    

        

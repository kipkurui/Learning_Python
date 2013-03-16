'''(60%)Create a program that receive as many sequences as the user wants
and calculates the GC ratio of each sequence. It should displays the
sequences in order of its GC ratio, with the G's and C's in upper case
and the T's and A's in lower case and in front of the sequence the
calculated GC ratio.Finally it should show was the avarage GC ration
among all the sequences.'''

from question2 import input_seq
from question2 import count
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
    print "%s : %5.3f " %(dic[keys[i]],keys[i])
print "The avarage GC content is %5.3f:"% (sum(keys)/len(keys))
    

        

'''(60%)Create a program that receive as many sequences as the user wants
and calculates the GC ratio of each sequence. It should displays the
sequences in order of its GC ratio, with the G's and C's in upper case
and the T's and A's in lower case and in front of the sequence the
calculated GC ratio.Finally it should show was the avarage GC ration
among all the sequences.'''
import gcmodules
sequences = gcmodules.input_seq()
nuccount = gcmodules.count(sequences)
gcrat = gcmodules.GC_ratio(nuccount)
dispnuc = gcmodules.replace(sequences)
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
    

        

import gcmodules
sequences = gcmodules.input_seq()
lists = gcmodules.count(sequences)
#formatting display
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

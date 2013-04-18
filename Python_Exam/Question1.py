#Prints number incremented by 2 and 3 alternating
m=1
k=0
n=int(raw_input("Enter a number: "))
print "The first",n,"items of the sequence are: "
print 1
while k <n-1:
    m+=2
    k+=1
    print m
    m+=3
    k+=1
    print m
    
    

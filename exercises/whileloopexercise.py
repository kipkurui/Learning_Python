"""
#1. This is an infinite loop bacause i will always be less than 32, it has no stop
#2 an increment of i so that i reaches a point where i is not a factor of 32
print "This is question 2"
i = 1
while i < 32:
    if 32%i == 0:
        print i, "is a factor of 32"
        i = i + 1
    else:
        print i, "is not a factor of 32"
        i = i + 1
#3.
print "This is question 3"
count = 0
while count <= 100:
    print "repeat",
    count = count + 1
#4.
print "This is question 4"
i = 1
while i <=10:
	print i,
	i = i + 1

#5.
print "This is question 5"
i = 1
end = int(raw_input("Enter the last number of the list"))
while i < end:
    print i,
    i = i + 1

#6.
print "This is question 6"
i = 1
add = 0
end = int(raw_input("Enter: "))
while i < end:
    add = add + i
    i = i + 1
print add

#7.
print "This is question 7"
i = int(raw_input("Enter start no"))
add = 0
end = int(raw_input("Enter: "))
while i < end:
    add = add + i
    i = i + 1
print add

#8.
print "This is question 8"

nucseq = raw_input("Enter a nuc sequence: ")
print nucseq.upper()
def lowerbase(base):
    if base == 'g' or base =='G':
        return 'g'
    elif base == 'a' or base =='A':
        return 'a'
    elif base == 'c' or base =='C':
        return 'c'
    else:
        return 't'
counter = 0
seq = 'atgGAtCat'
seq2 = ''
while counter < len(seq):
    seq2 = seq2+lowerbase(seq[counter])
    counter = counter + 1
print seq2

'''
nucseq = raw_input("Enter a nuc sequence: ")
bases ="ACTG"
newbases = ''
i = 0
while i < range(len(nucseq)):
    while i in nucseq:
        if i in nucseq:
            newbase = nucseq + i
            i +=1
        elif i == 'a' or i == A:
            newbase = newbase + 'A'
            i +=1
        elif i == 'c':
            newbase = newbase + 'C'
            i +=1
        elif i == 'g':
            newbase = newbase + 'G'
            i +=1

        else:
            newbase = newbase + 'T'
            i +=1
            
print newbases
'''
#9  and 10 (option 1)
print "This is question 9 and 10 (option 1)"
random = raw_input("Enter a sequence of NOs: ").strip()
print min(random)
random = '0'
rand = []
counter = 0
while random != "":
    print "first",counter
    counter =  counter + 1
    print "second",counter
    random = raw_input("Enter a no: ")
    if random   != "":
        rand = rand + [random]
        print rand
print "minimum no is : ", min(rand)
sum = 0
for i in rand:
    sum = sum + int(i)
print "Average is", sum/(counter-1)
print counter



#9 and 10(option 2)
print "This is question  9 and 10 (option 2)"

no = raw_input("Enter first number: ")
total = int(no)
smallest = no
counter = 1
while no != "":
    counter = counter +1
    no = raw_input("Enter a no: ")
    if no != "":
        total = total + int(no)
    if no != "" and int(no) < int(smallest):
        smallest = no
    
    print "smallest: ",smallest
    print "total =: ", total
    print "Average =: ", total/(counter-1)
    
##
##while names != "":
##    counter =  counter + 1
##    names = raw_input("Enter a name: ")
##    if names   != "":
##        listnames = listnames + [names]
##        print names   
##print listnames
##while i in listnames:
##    if len([i]) > len([i]+[1]):
##        shortest = i+1
##        print 
##        i = listnames([i] + [1]
##print shortest

###11.
print "This is question 11" 
names = raw_input("Enter first name: ")
first = names
shortest = names
longest = names
last = names
while names != "":
    names = raw_input("Enter a name: ")
    if names!='0'and names != "" and names > last:
        last = names
    print "Lastname: ",last
    if names!='0'and names != "" and names < first:
        first = names
    print "First name: ",first
    if names != "" and len(names) < len(shortest):
        shortest = names
    print "Shortest: ",shortest
    if names!='0'and names != "" and len(names) > len(longest):
        longest = names
    print "Longest: ",longest
        
#12. (option 1)
print "This is question 12 (option 1)"
n1 = 1
n2 = 11
while n2 < 102:
    print range(n1, n2)
    n1 = n1 + 10
    n2 = n2 + 10
    
###12 (optin 2)
print "This is question 12 (option 2)"
number = 1
while number < 100:
    print number,
    number = number + 1
    if number%10 == 0:
        print number
        number = number + 1
#13.(option1)
##
##random = '0'
##rand = []
##counter = 0
##while random != "":
##    counter =  counter + 1
##    random = raw_input("Enter a no or y to repeat cycle: ")
##    if random   != "":
##        rand = rand + [random]
##        print rand
##    elif random == 'y':
##        print "Enter y to continue: "
##        
##    sum = 0
##for i in rand:
##    sum = sum + int(i)
##print "Average is", sum/(counter-1)

#13 (option 2)
##print "This is question13"
##no = raw_input("Enter first number: ")
##total = int(no)
##smallest = no
##counter = 1
##while no != "":
##    counter = counter +1
##    no = raw_input("Enter a no: ")
##    if no != "":
##        total = total + int(no)
##    if no == "":
##        continue
##        print " Enter 'y' to continue: "
##    if no == 'y':
##        continue
##        
##    print "total =: ", total
##    print "Average =: ", total/(counter-1)
##stopper = raw_input("Enter y to continue or anything to stop" )
##while stopper == 'y':
#13.
print "This is question13"
no = raw_input("Enter first number: ")
total = 0
counter = 1
while no != "":
    counter = counter +1
    if no != '':
        no = raw_input("Enter a no: ")
        print no
        if no != '':
            total = total + int(no)
        print "Average =: ", total/(counter-1)
    if no == "":
        no = raw_input("Enter y to continue" )
        if no == 'y':
            no = raw_input("Enter a no: ")
    else:
        exit

#14.
print "This is question14"
counter1 = 0
counter2 = 0
letters1 = 0
letters2 = 0
firstphrase = raw_input("Enter first phrase: ")
secondphrase = raw_input("Enter second phrase: ")
letter = raw_input("Enter letter to search: ")
while counter1 < len(firstphrase) and counter2 <len(secondphrase):
    if letter == firstphrase[counter1]:
        letters1 = letters1 + 1
        counter1 = counter1 + 1
    else:
        counter1 = counter1 + 1
    if letter == secondphrase[counter2]:
        letters2 = letters2 + 1
        counter2 = counter2 + 1
    else:
        counter2 = counter2 + 1

print letters1
print letters2
if letters1 > letters2:
    print firstphrase
else:
    print secondphrase
"""
#15
print "This is question15"
floats = raw_input("Enter a float: ")
total = float(floats)
counter = 1
while floats != "":
    counter = counter +1
    floats = raw_input("Enter a float: ")
    if floats != '':
        total = total + float(floats)
        mean = total/(counter)
    if floats == "":
        floats = raw_input("Enter sum or mean or quit" )
        if floats == 'sum':
            print total
        if floats == 'mean':
            print mean
        if floats == 'quit':
            floats = ""


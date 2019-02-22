x = int(raw_input("Enter number"))
if x > 10:
    print "X is bigger than 10"
elif x > 5:
    print "X is between 6 and 10"
else:
    print "X is less or equal to 5"

#1.

x = int(raw_input("Enter a number"))
y = int(raw_input("Enter another number"))
print x%y
if x%y == 0:
    print x, " is divisible by" , y
else:
    print x, "is not divisibl by ", y
#2.
"""
if name not in vip or staff list:
    print "You cant come in"
    """

#3. No because you cant compare an int and a string in that manner.

#4.
n1 = int(raw_input("Enter the first number: "))
n2 = int(raw_input("Enter the second number: "))

if n2 != 0:
    print float(n1/n2)
else:
    print " Cannot divide", n1, "by ", n2
#5
no1 = int(raw_input("Enter the 1st number: "))
no2= int(raw_input("Enter the 2nd number: "))
no3= int(raw_input("Enter the 3rd number: "))
no4= int(raw_input("Enter the 4th number: "))
no5= int(raw_input("Enter the 5th number: "))
largest = no1
smallest = no1

if largest < no2:
    largest = no2
if largest < no3:
    largest = no3
if largest<no4:
    largest = no4
else:
    largest = no5
print largest


#6.
if smallest > no2:
    smallest = no2
if smallest > no3:
    smallest = no3
if smallest>no4:
    smallest = no4
else:
    smallest = no5
print smallest
#8
year = int(raw_input("Enter a year in four digits: "))
if year%400 ==0:
    print year , "is a leap year"
elif year%100==0:
    print year, "is not a leap year"
elif year%4==0:
    print year, "is_leap_year"
else:
    print year, "is not_leap_year"
#9

##if phrase > 'small':
##        print "Bad punctuation"
##else:
##    print "OK"
    #or
phrase = raw_input("Enter a phrase")
capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if phrase[0] not in capitals:
    print "Bad punctuation"
else:
    print "OK"


#10.
sort = ''
n1 = raw_input("Enter the first name: ")
n2 = raw_input("Enter the second name: ")
n3 = raw_input("Enter the third name: ")

if n1>n2>n2:
    sort = n1
elif n2>n1>n:
    print sort
#11.
divisible = []
no = int(raw_input("Please enter a number: "))
for i in range(1, 10):
    if no%(i+1) ==0:
        divisible = divisible + [i]
        print divisible

               
        

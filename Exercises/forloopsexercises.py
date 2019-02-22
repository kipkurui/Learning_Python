#3
for i in range(100):
    print "repeat"
#4
for i in range(1,11):
    print i,
print
#5.
number = int(raw_input("Enter a number: "))
for i in range(1, number+1):
    print i,
print
#6.
number = int(raw_input("Enter a number: "))
sum = 0
for i in range(1, number+1):
    sum = sum + i
print sum
#7.
total = 0
n1 = int(raw_input("Enter no1: "))
n2 = int(raw_input("Enter no2: "))
for i in range(n1, n2+1):
    total = total + i
print total
#12
for i in range(1, 101):
        print i,
    if i%10 == 0:
        print

n1 = 1
n2 = 11
for i in range(n1, n2):
    print range(n1, n2)
    n1 = n1 + 10
    n2 = n2 + 10

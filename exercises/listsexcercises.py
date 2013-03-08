l = ['There', 'are', 9000000, 'bicycles', 'in', 'Beijing']
#1 there are six elements, using the command below
print len(l)
#2. on-sttring element is index 2
#3.['are', 9000000, 'bicycles']
#4.
months = ['Januay', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
no = int(raw_input("Enter month no:  "))
print "The", no, "Month is", months[no-1]
#5.
for i in range(101):
    print "repeat",
print

#6
name = raw_input("What is ur name: ")
no = int(raw_input("Enter a number: "))
for i in range(no):
    print name,
print

#7
for i in range(10):
    print i
#8
for i in range(1, 101):
    print i,
#9 
for i in range(2, 101, 2):
    print i
#10
for i in range(1, 101):
    print i
#11
months = ['Januay', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
no = int(raw_input("Enter month no:  "))
##for i in range(len(months)):
print  months[no-1], "has" , days[no-1], "days"

#12.
no = int(raw_input("Enter no btw 1 and 10"))
for i in range(1, 101):
    if i%no == 0:
        print i

#13.
no = raw_input("Enter size (no): ")
while no != "":
    for i in range(int(no)+1):
        print '*'*i
    no = raw_input("Enter size (no): ")
#14. 
no = raw_input("Enter size (no): ")
while no != "":
    for i in range(int(no),0, -1):
        j = int(no) - i
        print ' '*j +'*'*i
    no = raw_input("Enter size (no): ")

#15.
no = raw_input("Enter size (no): ")
while no != "":
    for i in range(int(no)+1):
        j = int(no) - i
        print ' '*j +'*'+'*'*i + '*'*i
    print ' '*i + '*' + ' '*i
    print ' '*i + '*' + ' '*i
    no = raw_input("Enter size (no): ")


#1 function my_function can be called by my_function()
#2. Functions are expressions, when they are called they
#3.
'''
>>> s = raw_input('Enter text: ')
Enter text: the people
>>> s
'the people'
>>> s = raw_input('Enter text: ')
Enter text: Programming is fun, loving it
>>> print s
Programming is fun, loving it
>>> print 's'
s
>>> n = raw_input('Enter a number: ')
Enter a number: 45
>>> print int(n)*2
90
>>> exit()
'''
#4.
def greeting(name):
	#name = raw_input("Please enter your name: ")
	print "Hello ", name
greeting('Caleb')
name = raw_input('What is your name? ')
print "Hello", name


#5.
n1 = int(raw_input('Enter the first number: '))
n2 = int(raw_input('Enter the second number: '))
print "The sum is", n1+n2

#6
##n1 = int(raw_input('Enter the first number: '))
##n2 = int(raw_input('Enter the second number: '))
print "The difference is: ", n1-n2

#7.
##n1 = int(raw_input('Enter the first number: '))
##n2 = int(raw_input('Enter the second number: '))
print "The product is: ", n1*n2


#8.
n1 = int(raw_input('Enter a number: '))
n2 = raw_input('Enter some text: ')
print  n1*n2

#The question can be answered by defining a function
def maths(n1, n2):
    n1 = int(raw_input('Enter the first number: '))
    n2 = int(raw_input('Enter the second number: '))
    product = n1*n2
    sums = n1+n2
    difference = n1-n2
    print "Product: ", product
    print "sums: ", sums
    print "differences: " , difference
maths(n1, n2)

    
def greeting(name):
    print "Hello ", name
into = raw_input("Name?")
greeting(into)

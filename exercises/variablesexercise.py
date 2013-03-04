#1. Assignment statement passes value of the expression to the right of a variable to the variable
#2. Basic variable types in Python are:
'''
    1.integers
    2.Floats
    3.Booleans
    4.strings
    5.None type

'''
#3. an in variable i = 7
i = 7
print i/4
#the answer is 1 because, since both are of int type python returns an in

#4. By using the %(modulo) sign.
#using the above variable i
print i%4

#5.
date = raw_input() 
daysofweek = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
daysofweek = daysofweek*4
#print daysofweek
day = daysofweek[int(date)-1]
print day    


x = 'x'*100
print x

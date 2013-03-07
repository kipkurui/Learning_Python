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
date = raw_input("Please enter a numberbe tween 1 and 31 inclusive") 
daysofweek = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
daysofweek = daysofweek*5
#print daysofweek
day = daysofweek[int(date)-1]
print daysofweek
print day    

#6
x = 'x'*1000
print x

#7
s = "Harry's Hippie Hoedown"
print s + ": tickets only $5"
#This returns s concatenated to tickets only $5 to give:
#Harry's Hippie Hoedown: tickets only $5

#8. 
print s + ": tickets only $" + "5"*3
# returns >>>Harry's Hippie Hoedown: tickets only $555
#here is both concatenation of strings and repetition

#9. ABBA
print "ABBA was a Swedish band popular during the 80's"[0:4]
#the first four characters are sliced off

#10. during t
print "ABBA was a Swedish band popular during the 80's"[-15:-7]
#slicing of the given index from the last towards the beginning

#11. BAAB was a Danish band unpopular during the 90's
s = "ABBA was a Swedish band popular during the 80's"
print "BAAB"+s[4:11]+"Danish"+s[18:24]+"un"+s[24:-4]+"90's"
#concatenates the sliced s strings to form a new sentence

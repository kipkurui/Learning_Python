#import itertools 
#1
'''
def celciustofahrenheit(temp):
    F = (temp*9/5.0) + 32
    return F
#2.
temp1 = int(raw_input("Input a value in celcius: "))
temp2 = int(raw_input("Input a value in celcius: "))
print 'C','\t','F'
for  temp in range(temp1, temp2+1):
        F = celciustofahrenheit(temp)
        print temp,'\t',F
#3

def yaxis(x,m,c):
    y = m*x + c
    return y
##print yaxis(2, 1, 0)
#4
print "X","\t","Y"
for x in range(1, 11):
    y= yaxis(x,2,0)
    print x,"\t", y
    
#5 #Create a multiplication table
for i in range(1,11):           # i keep track of row 
    for j in range(1, 11):      # j keeps track of column
        print i*j,'\t',         # '\t' introduces tab after each print
    print                       #print a new line after each loop of j


def metropoly(c,p,i):
    if (c == 'yes' and p > 100000) or (c == 'no' and p > 200000 and i > 720000000):
        status = "metropoly"
        print name, "is a metropoly"
    elif c == 'no' and p < 200000:
        status = "not_metropoly"
        print name, "is not a metropoly because its not a capital with populationless than 200k"
    elif p<100000:
        status = "not_metropoly"
        print name,  "not a metropoly, population less than 100k"
    else:
        print name, "is not a metropoly, not a capital with income less than 72000000"
        return status
    '''
def metropoly(c,p,i):
    ismetropoly = []
    not_metropoly = []
    if (c == 'yes' and p > 100000) or (c == 'no' and p > 200000 and i > 720000000):
        ismetropoly.append(name)
        #print name, "is a metropoly"
    elif c == 'no' and p < 200000:
        not_metropoly.append(name)
        status = "not_metropoly"
        #print name, "is not a metropoly because its not a capital with populationless than 200k"
    elif p<100000:
        status = "not_metropoly"
        #print name,  "not a metropoly, population less than 100k"
    else:
        #print name, "is not a metropoly, not a capital with income less than 72000000"
        return status
    return ismetropoly

name = []
capital = []
pop = []
income= []
status = ''
for j in range(1):
    name = name + [raw_input("Enter name of a city: ")]
    capital =capital + [raw_input("Is it capital (yes or no): ")]
    pop = pop + [int(raw_input("What is the population of the city? "))]
    income =income+ [int(raw_input("Whats the per year income average? "))]

for c,p,i,name in zip(capital,pop,income,name):
    status = metropoly(c,p,i)
    print status
    

if status == 'metropoly':
    print name



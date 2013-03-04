def maxi(n1, n2):
    '''
    >>maxi(12, 15)
    15
    >>maxi(498, 300)
    498
    >>maxi(2000, 4)
    200
    '''
    if (type(n1) == str)  or (type(n2) == str):
        return "Error - can't compare strings to integers"
    elif n1 == n2:
        print "These numbers are equal!"
    
    elif n1 > n2:
        return n1
    else:
        return n2
                

test1 = maxi(498, 300)
print test1

##print "The greatest number in test1 is ", test1
    

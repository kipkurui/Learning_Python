def donuts(count):
    '''
    int ->str
    Returns the number of donuts rturning
    many if they are greater 
    
    '''
    #We need to convert the int count to string using str(count)
    s = "Number of donuts = "
    if count >= 10:
        return s+"Many"
    else:
        return s+str(count)

test1 = donuts(5)
test2 = donuts(10)
test3 = donuts(20)

print  test1
print  test2
print test3

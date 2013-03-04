def both_ends(string):
    '''
    
    Returns the first and the last two characters of a string
    >>string1 = both_ends('Welcome')
    Weme
    >>string2=both_ends('string')
    stng
    '''
    s = string[:2]+string[-2:]
    return s
string2=both_ends('string')       
string1 = both_ends('Welcome')
print string1, string2

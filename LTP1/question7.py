#question 7
def vowels(char):
    ''' str ->Boolean
    >>vowels('r')
    False
    >>vowels('a')
    True
    '''

    vowels = [ 'a', 'e' ,'i', 'o', 'u']
    if char in vowels:
        return True
    else:
        return False
#question 8  
def sume(lis):
    '''
    >>sum([1, 2, 3, 4])
    10
    
    '''
    total = sum(lis)
    return total


def mysum(mynos):
    total = 0
    for i in mynos:
        total = total + i
    return total

    

    
def multiply(mynos):
    '''
    >>multiply([1, 2, 3, 4])
    24
    '''
    total = 0
    for i in mynos:
        total = total * i
    return total
    
    
#question 9    
def reverse(string):
    ''' str -> str
    Return the  reverse of string

    >>>reverse('caleb'
    belac
    >>reverse('is it working')
    
    
    '''
    reversed = ''
    for char in string:
        reversed = char + reversed
    return reversed



#question 10
def generate_n_chars(n, c):
    '''
    
    >>generate_n_chars(5, 'p')
    'ppppp'
    '''
    repeat = n*c
    return repeat

#question 11
def average_len(mylists):
    '''
    >>average_len(['abc', 'python', 'two'])
    4
    '''
    den = len(mylist)
    words = 0
    for i in mylist:
        words = words + len(i)
    return float(chars)/den


#question 12
def remove_doubles(s):
    '''
    >>remove_doubles(
    '''
    clean = s[:1]
    for i in s[1:]:
        if i <> clean[-1]:
            clean = clean + [i]
    return clean








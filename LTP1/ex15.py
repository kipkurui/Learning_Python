myfile = 'In_flanders.txt'
from_file = file(myfile, 'r')
contents = from_file.read()

from_file.close()

words = contents.split() #to make each word in the test countable 
total_words = len(words)
total_chars = len(contents)


avarage_words = float(total_chars)/total_words

print contents
print total_chars
print total_words
print avarage_words


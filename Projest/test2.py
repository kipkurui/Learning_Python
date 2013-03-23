# sort strings in a list, case insensitive
import string
wordList = ['Python', 'is', 'really', 'great', 'stuff']
print "Original list:"
print wordList
wordList.sort()
print "After standard sort (ASCII upper case is before lower case):"
print wordList
wordList.sort(lambda x, y: cmp(string.lower(x), string.lower(y)))
print "After case insensitve sort with lambda and lower:"
print wordList

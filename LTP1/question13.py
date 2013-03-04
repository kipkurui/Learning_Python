import functions    #imports the functions i had earlier defined
                    #for use in this program
import sys          #imorts the function sys

filename = sys.argv[0]
f =file(filename)
for s in f:
    reverse_s = functions.reverse(s)
    print reverse_s
f.close()

myfile = 'In_flanders.txt'
to_file = 'new_file.txt'

from_file = file(myfile, 'r')
contents = from_file.readlines()

from_file.close()

to_file = file(to_file, 'w')

n = 1
for line in contents:
    if line <> '\n':
        to_file.write(str(n) + line)
        n = n + 1
    

to_file.close()



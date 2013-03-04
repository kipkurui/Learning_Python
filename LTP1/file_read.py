filename = "/home/Caleb/sample.txt"

f = file(filename)

x = []
y = []
z = []

for s in f:
    if s[0]<>'#':
        l = s.split()
        print "l=", l
        if  len(l) == 2:
            x.append(float(l[0]))
            y.append(float(l[1]))
            z.append(float(l[1]))
    else:
        print "Invalid data line: ", s

f.close()

print "x=", x
print "y=", y
print "z=", z

result = []
for i in range(len(x)):
    result.append(x[i]*y[i]*z[i])

w = file("/home/Caleb/output.txt", "w")
for i in range(len(x)):
         w.write("%f %f %f %f\n" % (x[i], y[i], z[i], result[i]))

w.close()

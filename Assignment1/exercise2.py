from exercise1 import celciustofahrenheit
temp1 = int(raw_input("Input a value in celcius: "))
temp2 = int(raw_input("Input a value in celcius: "))
print 'C','\t','F'
for  temp in range(temp1, temp2+1):
        F = celciustofahrenheit(temp)
        print temp,'\t',F

no1 = int(raw_input("Enter the 1st number: "))
no2= int(raw_input("Enter the 2nd number: "))
no3= int(raw_input("Enter the 3rd number: "))
no4= int(raw_input("Enter the 4th number: "))
no5= int(raw_input("Enter the 5th number: "))
largest = no1
smallest = no1

if largest < no2:
    largest = no2
if largest < no3:
    largest = no3
if largest<no4:
    largest = no4
else:
    largest = no5
print largest


#6.
if smallest > no2:
    smallest = no2
if smallest > no3:
    smallest = no3
if smallest>no4:
    smallest = no4
else:
    smallest = no5
print smallest

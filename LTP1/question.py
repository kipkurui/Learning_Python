#This is a solution to question 1

cost = -44.5         #cost of meal
tax = 6.75/100.00   #Local tax rate
tip = 0.10          #10% tip

#DEFINING FUNCTIONS

def calculate_pay(cost, tax, tip):
    print 'Culculating! Using cost=%f, tax=%f, and tip=%f' %(cost, tax, tip)                        #function that takes 3 arguments - def = define function
    if cost<0:
        print "Error: Cost shouldn't be negative!"
        return
    elif cost>200:
        print "That is an expensive meal!"
    total = cost + cost*tax
    pay = total + total*tip
    return pay

pay1 = calculate_pay(cost, tax, tip)
print "First: A meal of R%.2f is going to cost me R%.2f" % (cost, pay1) # changes the figure to 2 decimal places
cost2 = -20.00
if cost2<0:
    print "cant caculate price"
else:
    pay2 = calculate_pay(cost2, 0.875, 0.05)
cost3 = 340.00
pay3 = calculate_pay(cost3, 0.875, 0.05)
print "A meal of R%.2f is going to cost me R%.2f" % (cost3, pay3)

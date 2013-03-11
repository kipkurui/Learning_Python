names = []
capital = []
pop = []
income= []
ismetropoly = []
not_metropoly = []
for j in range(1):
    names = names + [raw_input("Enter name of a city: ")]
    capital =capital + [raw_input("Is it capital (yes or no): ")]
    pop = pop + [int(raw_input("What is the population of the city? "))]
    income =income+ [int(raw_input("Whats the per year income average? "))]
smallest = 6000000
metlpop = 'Nocity'
moreincome = -1
notmetrich = 'Nocity'
bigpop = 0
capbigpop = 'Nocity'

for j in range(len(names)):
    c = capital[j]
    p = pop[j]
    i = income[j]
    name = names[j]
    if (c == 'yes' and p > 100000) or (c == 'no' and p > 200000 and i > 720000000):
        ismetropoly.append(name)
        if p < smallest:
            smallest = p
            metlpop = name
    if (p < 100000) or (c == 'no' and p < 200000 and i < 72000000)or (c == 'no' and p < 200000) or (c == 'no' and i < 72000000) :
        not_metropoly.append(name)
        if i > moreincome:
            moreincome = i
            notmetrich = name
    if c == 'yes' and p >bigpop :
        bigpop = p
        capbigpop = name
if metlpop == 'Nocity':
    print "No metropoly to determine population"
if notmetrich == 'Nocity':
    print "All cities are metropolis"
if capbigpop == 'Nocity':
    print "No capital to determine population"
print "The list of metropolis is: ",ismetropoly
print "The metropoly with less population is ",metlpop
print "The richest non-metropoly is ", notmetrich
print "The most populos capital city is " ,capbigpop

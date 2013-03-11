def metropoly(c,p,i):
    if (c == 'yes' and p > 100000) or (c == 'no' and p > 200000 and i > 720000000):
        status = "metropoly"
        print name, "is a metropoly"
    elif c == 'no' and p < 200000:
        status = "not_metropoly"
        print name, "is not a metropoly because its not a capital with populationless than 200k"
    elif p<100000:
        status = "not_metropoly"
        print name,  "not a metropoly, population less than 100k"
    else:
        print name, "is not a metropoly, not a capital with income less than 72000000"
        return status

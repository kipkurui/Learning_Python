healthy_dat=[['P06457', '0.40', '0.54', '0.62\n'], ['P12345', '1.23', '2.32', '1.78\n'], ['P09876', '2.22', '3.33', '4.44\n'], ['P24680', '1.01', '1.02', '1.03\n']]
infected_dat=[['P06457', '0.48', '0.52\n'], ['P12345', '1.85', '1.97\n'], ['P09876', '1.01', '1.29\n'], ['P24680', '2.12', '2.30\n']]
def calcavarage(prot,prot2):
    Healthy={}
    for i in prot:
        lists=[]
        for j in range(1,len(i)):
            lists+=[float(i[j])]
        ava=sum(lists)/len(lists)
        Healthy[i[0]]=[ava]
    for i in prot2:
        lists=[]
        for j in range(1,len(i)):
            lists+=[float(i[j])]
        ava=sum(lists)/len(lists)
        Healthy[i[0]]+=[ava]
    return Healthy
def calcdelta(prot):
    Delta={}
    for key in prot:
        delta=prot[key][1]-prot[key][0]
        Delta[key]=delta
    return Delta
Healthy=calcavarage(healthy_dat,infected_dat)
Delta=calcdelta(Healthy)

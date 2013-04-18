import os
import sys
def validatepath(cond):
    '''->File path
    Validates the existence of the path and return the path
    '''
    flag = True
    while flag:
        paths = raw_input("Path of expression for "+str(cond)+" patients: ")
        if os.path.exists(paths)and os.path.isfile(paths):
          flag = False
    else:
        return paths
def menu():
    '''
    Load the menu
    '''
    print "Select an option"
    print "  [T] Select threshold value"
    print "  [D] Display categorised proteins odered by delta"
    print "  [F] Create 3 files with different categories"
    print "  [X] Exit"
    option=raw_input(":")
    return option
def Changeth(th=1.0):
    '''-int
    changs value of th
    '''
    if th==1.0:
        return th
    else:
        th=float(raw_input("New value for threshold: "))
        print "The threshold has been successfully changed to",th
        return th

def infohealthy(cond):
    path=validatepath(cond)
    healthy=open(path,"r")
    healthy_dat=[]
    for line in healthy:
        data=line.split(" ")
        healthy_dat+=[data]
    print "The", path, "contains expression level for", len(healthy_dat)," proteins in", (len(healthy_dat[0])-1), "patients" 
    return healthy_dat
def infoinfected():
    infected=open(validatepath("healthy"),"r")
    infected_dat=[]
    for line in healthy:
        data=line.split(" ")
        infected_dat+=[data]
    return infected_dat    
        
def optionD(Delta,th):
    #summary=[]
    print "List using threshold of",th
    print "Over expressed proteins: "
    over=[]
    for key in Delta:
        if th<Delta[key]:
            print key, "(",Delta[key],")"
            over+=key
    #summary+=over
    print "Normally expressed proteins: "
    normal=[]
    for key in Delta:
        if (-th)<Delta[key]<th:
            print key, "(",Delta[key],")"
            normal+=key
    #summary+=normal
    print "Under expressed proteins: "
    under=[]
    for key in Delta:
        if Delta[key]<(-th):
            print key, "(",Delta[key],")"
            under+=key
    #summary+=under
    #return summary
def summary(Delta,th):
    summary=[]
    #print "List using threshold of",th
    #print "Over expressed proteins: "
    over=[]
    for key in Delta:
        if th<Delta[key]:
            #print key, "(",Delta[key],")"
            over+=[key]
    summary+=[over]
    #print "Normally expressed proteins: "
    normal=[]
    for key in Delta:
        if (-th)<Delta[key]<th:
            #print key, "(",Delta[key],")"
            normal+=[key]
            #print key
            #print normal
    summary+=[normal]
    #print "Under expressed proteins: "
    under=[]
    for key in Delta:
        if Delta[key]<(-th):
            #print key, "(",Delta[key],")"
            under+=[key]
    summary+=[under]
    return summary

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
def export(summary):
    predix=raw_input("What is the predix of the files: ")
    normal=open(str(predix)+"_NORMAL.txt","w")
    for i in summary[1]:
        normal.write(i)
    over=open(str(predix)+"_OVER.txt","w")
    for i in summary[0]:
        over.write(i,",")
    under=open(str(predix)+"_UNDER.txt","w")
    for i in summary[2]:
        under.write(i)
    print "The files",predix+"_NORMAL.txt",predix+"_OVER.txt and ",predix+"_UNDER.txt have been successfully created"
    
##########MAIN##########
healthy_dat=infohealthy("healthy")
infected_dat=infohealthy("infected")
Healthy=calcavarage(healthy_dat,infected_dat)
Delta=calcdelta(Healthy)
option=menu()
th=1.0
while option.upper()!="X":
    if option.upper()=="D":
        optionD(Delta,th)
        option=menu()
    elif option.upper()=="T":
        th=Changeth("new")
        option=menu()
    elif option.upper()=="F":
        summarries=summary(Delta,th)
        export(summarries)
        option=menu()
    else:
        print "Invalid choice"
        option=menu


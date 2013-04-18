list_x=[("PSG", "Barcelona", 2, 2),("Bayern Munchen", "Juventus", 2, 0),
        ("Malaga", "Borusia Dortmund", 0, 0),("Real Madrid", "Galatasaray", 3,0)]
def getpoint(scores):
    Draw=[]
    for i in scores:
        if i[2]==i[3]:
            point=(i[0],1)
            Draw+=[point]
            point=(i[1],1)
            Draw+=[point]
        if i[2]>i[3]:
            point=(i[0],3)
            Draw+=[point]
            point=(i[1],0)
            Draw+=[point]
        if i[2]<i[3]:
            point=(i[0],0)
            Draw+=[point]
            point=(i[1],3)
            Draw+=[point]
    return Draw
        
print getpoint(list_x)
    

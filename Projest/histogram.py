PDB = {'SequeceA': 'YNFFPRKPKWDKNQITYRIIGYTPDLDPETVDDAFARAFQVWSDVTPLRFSRIHDGEADIMINFGRWEHGDGYPFDGKDGLLAHAFAPGTGVGGDSHFDDDELWTLGKGVGYSLFLVAAHAFGHAMGLEHSQDPGALMAPIYTYTKNFRLSQDDIKGIQELYGASPD',
       'SequeceB': 'ISYGNDALMP', 'ThreeSeqA': ' TYR ASN PHE PHE PRO ARG LYS PRO LYS TRP ASP LYS ASN GLN ILE THR TYR ARG ILE ILE GLY TYR THR PRO ASP LEU ASP PRO GLU THR VAL ASP ASP ALA PHE ALA ARG ALA PHE GLN VAL TRP SER ASP VAL THR PRO LEU ARG PHE SER ARG ILE HIS ASP GLY GLU ALA ASP ILE MET ILE ASN PHE GLY ARG TRP GLU HIS GLY ASP GLY TYR PRO PHE ASP GLY LYS ASP GLY LEU LEU ALA HIS ALA PHE ALA PRO GLY THR GLY VAL GLY GLY ASP SER HIS PHE ASP ASP ASP GLU LEU TRP THR LEU GLY LYS GLY VAL GLY TYR SER LEU PHE LEU VAL ALA ALA HIS ALA PHE GLY HIS ALA MET GLY LEU GLU HIS SER GLN ASP PRO GLY ALA LEU MET ALA PRO ILE TYR THR TYR THR LYS ASN PHE ARG LEU SER GLN ASP ASP ILE LYS GLY ILE GLN GLU LEU TYR GLY ALA SER PRO ASP', 'ThreeSeqB': ' ILE SER TYR GLY ASN ASP ALA LEU MET PRO',
 'Title': 'Title: CRYSTAL STRUCTURE OF MMP-2 ACTIVE SITE MUTANT IN COMPLEX WITH APP- DRIVED\n DECAPEPTIDE INHIBITOR'}
count_of_aa=[]
aas= ["Ala","Arg","Asn","Asp","Asx","Cys","Gln","Glu","Glx","Gly","His",
      "Ile","Leu","Lys","Met","Phe","Pro","Ser","Thr","Trp","Tyr","Val"]
sequence = PDB['ThreeSeqA']+PDB['ThreeSeqB']
for i in aas:
    count=sequence.count(i.upper())
    count_of_aa+=[(i,count)]

def sort_by(seq,i,sort):
    seq = sorted(seq, key=lambda x: x[i], reverse = sort)            
    for i in seq:
        if i[1] !=0:
            print "%s (%3i) : %s"% (i[0],i[1],"*"*i[1])

sort_by_an(count_of_aa,0,False)
##aas.sort(cmp=None, key=None, reverse=True)
##for i in aas:
##    count=sequence.count(i.upper())
##    histogram[i]=count
##print histogram
##for i in aas:
##    if histogram[i]!=0:
##        print "%s (%3i) : %s"% (i,histogram[i],"*"*histogram[i])
##lists = []
##for key in histogram:
##    lists+=[(key,histogram[key])]
##print lists 
##count_of_aa = sorted(lists, key=lambda x: x[1], reverse = True)
##for i in lists:
##    if i[1]!=0:
##        print "%s (%3i) : %s"% (i[0],i[1],"*"*i[1])
##
##histolist =[]
##for key in histogram
##from collections import OrderedDict
##Shistogram = OrderedDict(sorted(histogram.items(), key=lambda x: x[1]))
##for k, v in Shistogrhiam.items():
##    print "%s (%3i) : %s"% (k,v,"*"*v)

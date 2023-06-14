import csv
import re
def cleaning(array):
    newarray = []
    for item in array:
        newitem = re.sub('\s+',' ',item)
        newarray.append(newitem)
    #print(newarray)    
    return newarray


def Abbreviation(fibrecompArr):
    newlist = []
    abblist = [('POLY ' , 'POLYESTER') , ('NYLN ' , 'POLYAMIDE'),
('VSCS ' ,'VISCOSE'),('SPX ' ,'ELASTANE'),('CTN ' , 'COTTON')]
    #print(type(abblist))
    #split the full composition into wording.
    for fibrestring in fibrecompArr:
        fibre= fibrestring.split()
        for word in fibre:
                for item in abblist:
                    if item[1] == word:
                        fibre[fibre.index(word)] = item[0]
                
        newfibre = ' '.join(fibre)
        newlist.append(newfibre)                
        print(newlist)
        #print(fibrecompArr)
    return  newlist
    
def SortoutinColmun(fibrecsv,fibrecomp):
    colmun = []
    with open(fibrecsv, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        colmun = [row[fibrecomp] for row in reader]
        
    csv_file.close()
    #print(colmun )
    
    return colmun



        



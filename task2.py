import csv
import re
def cleaning(array):
    newarray = []
    for item in array:
        newitem = re.sub('\s+',' ',item)
        rmEOD = re.sub('\((.*?)\)','',newitem)
        newarray.append(rmEOD)
      
    return newarray


def Abbreviation(fibrecompArr):

    newlist = []
    abblist = [('POLY ' , 'POLYESTER') , ('NYLN ' , 'POLYAMIDE'),
('VSCS ' ,'VISCOSE'),('SPX ' ,'ELASTANE'),('CTN ' , 'COTTON'),('','FABRIC')]
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
        #print(newlist)
        #print(fibrecompArr)
    return  newlist
    
def SortoutinColmun(fibrecsv,fibrecomp):
    colmun = []
    fieldnames = ["Product ID","Style","Fabric","Colour","Textile Content"]
    with open(fibrecsv, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        colmun = [row[fibrecomp] for row in reader]
        #use cleaning() function to remove excessive space so each word will only have one space in between.
        cleanedcolmun = cleaning(colmun)
        #use Abbreviation() to turn some of the fibre name into short form like turning POLYAMIDE to NLYN, turning POLYESTER to POLY...
        abbcolmun = Abbreviation(cleanedcolmun)
    csv_file.close()
    return abbcolmun


   
            
            
                
   
    





        



import csv
from task2 import *
#SortoutinColmun() 
#cleaning()
#Abbreviation()
def updatecsv(csvfile,fibrecomp,data):

    with open(csvfile,'w') as file:
            writer = csv.writer(file)
            
            writer.writerow(data)
   


fibrecompArr = SortoutinColmun("Copy_zedonkfibre.csv",'Textile Content')
cleanedArr = cleaning(fibrecompArr)
data = Abbreviation(cleanedArr)
updatecsv("Copy_zedonkfibre.csv",'Textile Content',data)

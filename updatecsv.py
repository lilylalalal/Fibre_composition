import csv
import pandas as pd  
from task2 import*

def removecolomun(fibrecsv,newcsv):
    with open(fibrecsv, "r") as source:
        reader = csv.reader(source)
        with open(newcsv,'w') as result:
              writer = csv.writer(result)
              for row in reader:  
                  writer.writerow((row[0],row[1],row[2],row[3]))
                  
        result.close()
    source.close()
    return newcsv

def addcolumn(removedcolomun,fibrelist,title):
     data_new = pd.read_csv(removedcolomun)
     data_new[title] = fibrelist    
     data_new.to_csv('data_new.csv')   


fibrelist = SortoutinColmun("Copy_zedonkfibre.csv","Textile Content")
#print(fibrelist )
removedcolomun = removecolomun("Copy_zedonkfibre.csv","newfile.csv")
addcolumn(removedcolomun,fibrelist,"Textile Content")
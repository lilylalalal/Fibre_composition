import csv

def SortoutinColmun(fibrecsv,fibrecomp):
    colmun = []
    with open(fibrecsv, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        colmun = [row[fibrecomp] for row in reader]
        csv_file.close()
    csv_file.close()
    print(colmun )
    
    return colmun


SortoutinColmun("zedonkfibre.csv",'Textile Content')
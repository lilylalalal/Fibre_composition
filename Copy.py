import csv

def copyfile(csvfile,duplicatedcsv):
    with open(csvfile , "r") as file1:
        reader = csv.reader(file1)
        with open(duplicatedcsv,'w') as file2:
            writer = csv.writer(file2)
            for row in reader:
                writer.writerow(row)
        
        file2.close()
    file1.close()
    return duplicatedcsv
    

copyfile("zedonkfibre.csv","Copy_zedonkfibre.csv")
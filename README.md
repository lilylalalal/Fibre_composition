"Overveiw"
Zedonk data base has word count limit of 100 for each composition cell.
However, garment styles usually contain 2 or more fabric and trim item which need to disclose as a 
garment composition.
This task will help the generated composition list to streamdown the word count upto the Zedonk 
limit.
--------------------------------------------------------------------------------------------

Update Excel File (Master Line Sheet)

Read Excel file 
- Have openpyxl import load_workbook
-read the excel file
-appoint to the needed sheet(filename['sheet'])
-Loop in the sheet and appointed the needed row(row['SKU'])
-Pull the raw data into an array

pull data to the required sheet

##Fibre name abbreviation
"TASK ONE: Read & duplicate csv file - Copy(csvfile)"
-Importing csv library 
-Duplicate the fibercomp.csv file and read

"TASK TWO: find the fiber comp from the csv file and put into an array - SortoutinColmun(fibrecsv,fibrecomp)"
-Identify the 'Textile Content'(04) column 
-Pull the fibre content into the array "[fibrecompArr]"

"TASK TWO.FIVE: HELPER FUNCTION" 
Cleaning(Arr)
-Data cleaning by removing excessive spacing
-Removing extra info like (EOD),(EOS) ,(detail from the Other fibre)
Abbreviation(fibrecompArr)
-Add below Abbreviation tuple-list into the Abbreviation() function 
-Compare the fibrecompArr with each tuple.
-If the word match than change the tuple[1] means there is abbreviation avalible to simplfy the wording.
-Replace the tuple[0] as word
-Return newfibrecomp array
"Abbreviation Fibre list"
'POLY' : 'POLYESTER'
'NYLN' : 'POLYAMIDE'
'VSCS' : 'VISCOSE'
 'SPX' : 'ELASTANE'
 'CTN' : 'COTTON'
and more ...

simplfy(newfibrecompArr)
-newlist = []
-set 'maxcount' = 100
-Use For loop to count every newfibrecomp in the array.
-compare the newfibrecomp with 'maxcount'
-(helper fiunction may be needed in this step to further streamdown the newfibrecomp which exceed 
the maxcount)
-If any 'newfibrecomp' over 'maxcount' then helperfunction(newfibercomp)
- push it into 'newlist'
-return 'newlist'


"TASK THREE: write csv file with the new list "
Removecolomun(fibrecsv,newcsv)
-replace the "Textile Content" colmune with the "new list"
-removing the "Textile Content" from the old data
Addcolumn(removedcolomun,fibrelist,title)
- Add "Textile Content" with new fibre list (after simplfied)
-save and exit the csv file

#Upload Fibre_composition to ZeDonk
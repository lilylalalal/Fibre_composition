#Upload Fibre_composition to ZeDonk



##Fibre name abbreviation
"Overveiw"
Zedonk data base has word count limit of 100 for each composition cell.
However, garment styles usually contain 2 or more fabric and trim item which need to disclose as a 
garment composition.
This task will help the generated composition list to streamdown the word count upto the Zedonk 
limit.

"TASK ONE: Read csv file"
-Importing csv library 
-Duplicate the fibercomp.csv file and read

"TASK TWO: find the fiber comp from the csv file and put into an array
-Identify the 'Textile Content'(04) column 
-Pull the fibre content into the array "[fibrecompArr]"

"TASK THREE: Abbreviation(fibrecompArr)" *****
-Add below Abbreviation Dict into the Abbreviation() function 
-Compare the fibrecompArr with the Abbreviation list ****
-If the word/dict.value match than change the word to dict.key ******* 
-Return newfibrecomp array
"Abbreviation Fibre list"
'POLY' : 'POLYESTER'
'NYLN' : 'POLYAMIDE'
'VSCS' : 'VISCOSE'
 'SPX' : 'ELASTANE'
 'CTN' : 'COTTON'

 "TASK FOUR: textcount(newfibrecompArr)"
-newlist = []
-set 'maxcount' = 100
-Use For loop to count every newfibrecomp in the array.
-compare the newfibrecomp with 'maxcount'
-(helper fiunction may be needed in this step to further streamdown the newfibrecomp which exceed 
the maxcount)
-If any 'newfibrecomp' over 'maxcount' then helperfunction(newfibercomp)
- push it into 'newlist'
-return 'newlist'


"TASK FIVE: write csv file with the new list "
-replace the "Textile Content" colmune with the "new list"
-save and exit the csv file

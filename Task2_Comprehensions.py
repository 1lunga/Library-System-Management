#Lists

#Displaying the codes in a NORMAL LIST
print("NORMAL LIST")
ProgrammingBooks_codes = [14,15,16,17,18,19,20]
PBCList = []
for pbc in ProgrammingBooks_codes:
    PBCList.append(pbc)
print("ProgrammingBooks_codes:", PBCList)

#Adding Codes together for auditing purpose (NORMAL LIST)
PBCListAdd = []
sumLcodes = 0
for pbcsum in ProgrammingBooks_codes:
    sumLcodes = sumLcodes + pbcsum
PBCListAdd.append(sumLcodes)
print("All codes added together:", PBCListAdd)

#Displaying only codes tracked by odd numbers (NORMAL LIST)
PBCListOdd = []
for pbcOdd in ProgrammingBooks_codes:
    if pbcOdd % 2 != 0:
        PBCListOdd.append(pbcOdd)
print("Odd numbers in the list are:",PBCListOdd)



#Displaying the codes in a COMPREHENSIVE LIST
print("\nCOMPREHENSIVE LIST")
PBCCompList = [pbcCL for pbcCL in ProgrammingBooks_codes]
print("ProgrammingBooks_codes:", PBCCompList)

#Adding Codes together for auditing purpose (COMPREHENSIVE LIST)
sumCLcodes = 0
PBCCompListAdd = [sumCLcodes := sumCLcodes + pbcsumCL for pbcsumCL in ProgrammingBooks_codes]
print("All codes added together:", PBCCompListAdd)

#Displaying only codes tracked by odd numbers (COMPREHENSIVE LIST)
PBCCompListOdd = [pbcCLOdd for pbcCLOdd in ProgrammingBooks_codes if pbcCLOdd % 2 != 0] 
print("Odd numbers in the list are:",PBCCompListOdd)

#Sets

#Dispalaying lists of codes
booksList = set(ProgrammingBooks_codes)
print("\nProgrammingBooks_codes:", booksList)
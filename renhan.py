taipei = open(r"C:\Data\xuc\Python\taipei.alma", "r")
number_lines = 0
dictionary = {}

while True:
    line = taipei.readline()
    if not line:
        break
    a = line.find("EQ")
    b = line.find(" ", a + 3)
    eq = line[a + 3:b]
    fmt = ""
    c = line.find("FMT")
    d = line.find('"', c + 5) 
    fmt = line[c + 5:d]
    dictionary[eq] = fmt
    number_lines += 1
        
#print number_lines
#print dictionary
taipei.close()

import csv
with open(r"C:\Data\xuc\Python\tcl_alarms.csv", "rb") as csvfile:
    csvreader = csv.reader(csvfile)
    #for row in csvreader:
        #print row
    csvfile1 = open(r"C:\Data\xuc\Python\tcl_alarms1.csv", "wb+")
    csvwriter = csv.writer(csvfile1)
    i = 1
    for row in csvreader:
        format = None
        if i > 1:
            equate = row[13]
            if dictionary.has_key(equate):
                format = dictionary[equate]
            else:
                print "Missing Equate in ACT file:", equate
        else:
            format = "ACT Fromat"           
        i += 1
        row.insert(2, format)
        csvwriter.writerow(row)
    csvfile1.close()
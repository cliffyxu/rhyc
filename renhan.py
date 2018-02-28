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
    #dictionary.update({eq : None})
    fmt = ""
    c = line.find("FMT")
    d = line.find('"', c + 5) 
    fmt = line[c + 5:d]
    dictionary[eq] = fmt
    number_lines += 1
        
print number_lines
print dictionary
taipei.close()
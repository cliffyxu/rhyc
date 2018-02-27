taipei = open(r"C:\Data\xuc\Python\taipei.alma", "r")
number_lines = 0
dictionary = {}
while True:
    global number_lines, dictionary
    line = taipei.readline()
    if not line:
        break
    line1 = line.split()
    print line1
    number_lines += 1
print number_lines
print dictionary
taipei.close()
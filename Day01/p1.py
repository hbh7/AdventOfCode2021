inputfile = open("input.txt")
prevnum = -1
larger = 0
for line in inputfile:
    if prevnum != -1:
        if int(line) > prevnum:
            larger += 1
    prevnum = int(line)
print(larger)

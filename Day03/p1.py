inputfile = open("input.txt")

lines = []
gamma = ""
epsilon = ""

for line in inputfile:
    lines.append(line)

for i in range(len(lines[0]) - 1):
    zeroes = 0
    ones = 0
    for k in range(len(lines)):
        if lines[k][i] == "0":
            zeroes += 1
        else:
            ones += 1
    if zeroes > ones:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"


print(gamma)
print(epsilon)

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma)
print(epsilon)
print(gamma * epsilon)

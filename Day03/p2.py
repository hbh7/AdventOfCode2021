inputfile = open("input.txt")

lines = []
gamma = ""
epsilon = ""

for line in inputfile:
    lines.append(line)

# Calculate oxygen generator rating
ox_lines = lines.copy()
for i in range(len(lines[0]) - 1):
    if len(ox_lines) == 1:
        break
    zeroes = 0
    ones = 0
    for k in range(len(ox_lines)):
        if ox_lines[k][i] == "0":
            zeroes += 1
        else:
            ones += 1

    newlines = []
    if zeroes > ones:
        # Only re-add lines with the target bit as zero
        for k in range(len(ox_lines)):
            if ox_lines[k][i] == "0":
                newlines.append(ox_lines[k])
    else:
        # Only re-add lines with the target bit as one
        for k in range(len(ox_lines)):
            if ox_lines[k][i] == "1":
                newlines.append(ox_lines[k])
    ox_lines = newlines

# Calculate CO2 scrubber rating
co2_lines = lines.copy()
for i in range(len(lines[0]) - 1):
    if len(co2_lines) == 1:
        break
    zeroes = 0
    ones = 0
    for k in range(len(co2_lines)):
        if co2_lines[k][i] == "0":
            zeroes += 1
        else:
            ones += 1

    newlines = []
    if zeroes < ones or zeroes == ones:
        # Only re-add lines with the target bit as zero
        for k in range(len(co2_lines)):
            if co2_lines[k][i] == "0":
                newlines.append(co2_lines[k])
    else:
        # Only re-add lines with the target bit as one
        for k in range(len(co2_lines)):
            if co2_lines[k][i] == "1":
                newlines.append(co2_lines[k])
    co2_lines = newlines

print(ox_lines)
print(co2_lines)

ox = int(ox_lines[0], 2)
co2 = int(co2_lines[0], 2)

print(ox)
print(co2)
print(ox * co2)

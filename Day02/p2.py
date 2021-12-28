inputfile = open("input.txt")
horizontal = 0
depth = 0
aim = 0
for line in inputfile:
    parts = line.split(" ")
    if parts[0] == "forward":
        horizontal += int(parts[1])
        depth += aim * int(parts[1])
    elif parts[0] == "up":
        aim -= int(parts[1])
    elif parts[0] == "down":
        aim += int(parts[1])

print(horizontal)
print(depth)
print(horizontal * depth)

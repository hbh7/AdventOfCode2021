inputfile = open("input.txt")
prev_window_sum = -1
window = []
larger = 0
for line in inputfile:
    window.append(int(line))
    if len(window) > 3:
        window.pop(0)
    elif len(window) < 3:
        continue

    window_sum = window[0] + window[1] + window[2]

    if prev_window_sum != -1:
        if window_sum > prev_window_sum:
            larger += 1
    prev_window_sum = window_sum
print(larger)

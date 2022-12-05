inp_path = open("day4_input.txt", "r").read().split("\n")

overlap = 0

for sections in inp_path:
    pair = [s.split("-") for s in sections.split(",")]
    left, right = pair[0], pair[1]

    if int(left[0]) <= int(right[0]) and int(left[1]) >= int(right[1]):
        overlap += 1
    elif int(right[0]) <= int(left[0]) and int(right[1]) >= int(left[1]):
        overlap += 1

print(f"Part 1: {overlap}")

overlap2 = 0

for sections in inp_path:
    pair = [s.split("-") for s in sections.split(",")]
    left, right = pair[0], pair[1]
    leftr = range(int(left[0]), int(left[1]) + 1)
    rightr = range(int(right[0]), int(right[1]) + 1)

    if int(left[0]) in rightr or int(left[1]) in rightr:
        overlap2 += 1
    elif int(right[0]) in leftr or int(right[1]) in leftr:
        overlap2 += 1

print(f"Part 2: {overlap2}")

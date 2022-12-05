inp_path = open("day3_input.txt", "r").read().split("\n")
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = 0

for i in inp_path:
    part1 = i[len(i) // 2 :]
    part2 = i[: len(i) // 2]

    priority = {}

    for x in part1:
        if x in part2:
            priority[x] = alpha.index(x) + 1

    total += sum(priority.values())

print(f"Part 1: {total}")

# Part 2

total_p2 = 0
count = 0

priority = {}

for i in inp_path:

    for x in set(i):
        if x not in priority:
            priority[x] = 1
        else:
            priority[x] += 1

    total += sum(priority.values())

    count += 1

    if count == 3:
        count = 0
        maxkey = max(priority, key=priority.get)
        total_p2 += alpha.index(maxkey) + 1
        priority = {}

print(f"Part 2: {total_p2}")

# Day 1: Calorie Counting

inp_path = open("day1_input.txt", "r").read().split("\n\n")

# Part 1
max_load = 0
all_cals = []

for i in inp_path:
    elf_load = sum([int(i) for i in i.split("\n")])

    if elf_load > max_load:
        max_load = elf_load

    all_cals.append(elf_load)

print(f"Max calories: {max_load}")

# Part 2
print(f"Sum top 3 Most Cals: {sum(sorted(all_cals)[-3:])}")

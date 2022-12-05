import copy

inp_path = open("day5_input.txt", "r").read().split("\n")

cargo_base = {
    1: ["F", "D", "B", "Z", "T", "J", "R", "N"],
    2: ["R", "S", "N", "J", "H"],
    3: ["C", "R", "N", "J", "G", "Z", "F", "Q"],
    4: ["F", "V", "N", "G", "R", "T", "Q"],
    5: ["L", "T", "Q", "F"],
    6: ["Q", "C", "W", "Z", "B", "R", "G", "N"],
    7: ["F", "C", "L", "S", "N", "H", "M"],
    8: ["D", "N", "Q", "M", "T", "J"],
    9: ["P", "G", "S"],
}

cargo = copy.deepcopy(cargo_base)
cargo2 = copy.deepcopy(cargo_base)

# Part 1

for move in inp_path:
    commands = move.split(" ")
    load_size = int(commands[1])
    stack_pull = int(commands[3])
    stack_dest = int(commands[5])
    load_stack = []

    for i in range(load_size):
        load_stack.append(cargo[stack_pull].pop())

    cargo[stack_dest] += load_stack

# Part 2

for move in inp_path:
    commands = move.split(" ")
    load_size = int(commands[1])
    stack_pull = int(commands[3])
    stack_dest = int(commands[5])

    load_stack = cargo2[stack_pull][-load_size:]

    cargo2[stack_pull] = cargo2[stack_pull][:-load_size]
    cargo2[stack_dest] += load_stack


Ans1 = "".join([val[-1] for val in cargo.values()])
Ans2 = "".join([val[-1] for val in cargo2.values()])

print(f"Part 1: {Ans1}")
print(f"Part 2: {Ans2}")

# Communication system
# 4 unique Char Start of packet marker

inp_path = open("day6_input.txt", "r").read()


def communication(s):
    for i in range(s, len(inp_path) + 1):
        if len(set(inp_path[i - s : i])) == s:
            return i


print(f"Part 1: {communication(4)}")
print(f"Part 2: {communication(14)}")

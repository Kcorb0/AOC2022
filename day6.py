# Communication system
# 4 unique Char Start of packet marker

inp_path = open("day6_input.txt", "r").read()


def communication(s):

    cnt = s

    for i in range(s, len(inp_path) + 1):
        if len(set(inp_path[i - s : i])) == s:
            return cnt
        cnt += 1


print(f"Part 1: {communication(4)}")
print(f"Part 2: {communication(14)}")

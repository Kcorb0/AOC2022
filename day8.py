grid = open("day8_input.txt", "r").read().split("\n")

# visible = all trees surrounding are shorter
# Only check up, down, left, right
# Visible from the edge of the map

visible = 0

for row in range(0, len(grid)):
    for col in range(0, len(grid[0])):
        val = grid[row][col]

        if col == 0 or max(grid[row][:col]) < val:
            visible += 1
        elif col == len(grid[0]) - 1 or max(grid[row][col + 1 :]) < val:
            visible += 1

        elif row == 0 or max(grid[row][col]) < val:
            visible += 1

    break


# print(f"\n{visible}")

print(grid[0:][1])

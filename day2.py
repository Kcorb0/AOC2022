inp_path = open("day2_input.txt", "r").read().split("\n")

# A or X = Rock, B or Y = Paper, C or Z = Scissors
hands = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
wincon = {"A": "Y", "B": "Z", "C": "X"}
total_score = 0

for i in inp_path:
    match = i.split(" ")
    opp = match[0]
    you = match[1]

    if you == wincon[opp]:
        total_score += hands[you] + 6
    elif hands[you] == hands[opp]:
        total_score += hands[you] + 3
    else:
        total_score += hands[you]

print(f"Part 1: {total_score}")

# Part 2
# X = Lose, Y = Draw, Z = Win
losscon = {"A": "Z", "B": "X", "C": "Y"}

total_two = 0

for i in inp_path:
    match = i.split(" ")
    opp = match[0]
    outcome = match[1]

    if outcome == "Y":
        total_two += hands[opp] + 3
    elif outcome == "Z":
        total_two += hands[wincon[opp]] + 6
    else:
        total_two += hands[losscon[opp]]

print(f"Part 2: {total_two}")

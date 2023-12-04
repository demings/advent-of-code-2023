with open("4_input.txt") as f:
    lines = f.readlines()

cards = []
for line in lines:
    [winning_nums, your_nums] = line.split(":")[1].replace("\n", "").split("|")
    winning_nums = winning_nums.strip().split()
    your_nums = your_nums.strip().split()
    cards.append([winning_nums, your_nums])

points = 0
for card in cards:
    match_count = 0
    for your_num in card[1]:
        if your_num in card[0]:
            match_count += 1
    if match_count > 0:
        points += pow(2, match_count - 1)

print(points)
class Card:
    def __init__(self, id, winning_nums, your_nums):
        self.id = id
        self.winning_nums = winning_nums
        self.your_nums = your_nums


def get_cards() -> list[Card]:
    with open("4_input.txt") as f:
        lines = f.readlines()

    cards = []
    for idx, line in enumerate(lines):
        [winning_nums, your_nums] = line.split(":")[1].replace("\n", "").split("|")
        winning_nums = winning_nums.strip().split()
        your_nums = your_nums.strip().split()
        cards.append(Card(idx + 1, winning_nums, your_nums))

    return cards


cards = get_cards()

match_cache = {}
for card in cards:
    if card.id in match_cache.keys():
        match_count = match_cache[card.id]
    else:
        match_count = 0
        for your_num in card.your_nums:
            if your_num in card.winning_nums:
                match_count += 1
        match_cache[card.id] = match_count

    for i in range(match_count):
        cards.append(cards[card.id + i])

print(len(cards))

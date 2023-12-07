from functools import cmp_to_key, reduce

with open("7_input.txt") as f:
    lines = f.readlines()

hands = []
for line in lines:
    split = line.split()
    hands.append([split[0], int(split[1])])


def is_five(hand):
    return len(set(hand)) == 1


def is_four(hand):
    count1 = 0
    count2 = 0

    for card in hand:
        if card == hand[0]:
            count1 += 1
        elif card == hand[1]:
            count2 += 1

    return count1 == 4 or count2 == 4


def is_full(hand):
    return len(set(hand)) == 2


def is_three(hand):
    count1 = 0
    count2 = 0
    count3 = 0

    for card in hand:
        if card == hand[0]:
            count1 += 1
        elif card == hand[1]:
            count2 += 1
        elif card == hand[2]:
            count3 += 1

    return count1 == 3 or count2 == 3 or count3 == 3


def is_two(hand):
    return len(set(hand)) == 3


def is_one(hand):
    return len(set(hand)) == 4


def is_high(hand):
    return len(set(hand)) == 5


hand_types = {
    "five": is_five,
    "four": is_four,
    "full": is_full,
    "three": is_three,
    "two": is_two,
    "one": is_one,
}

card_types = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def get_hand_type_index(hand):
    for idx, key in enumerate(hand_types.keys()):
        if hand_types[key](hand):
            return idx
    return 6


def compare_hands(hand1, hand2):
    if get_hand_type_index(hand1) < get_hand_type_index(hand2):
        return 1

    if get_hand_type_index(hand1) > get_hand_type_index(hand2):
        return -1

    for idx, card in enumerate(hand1):
        if card_types[card] > card_types[hand2[idx]]:
            return 1
        if card_types[card] < card_types[hand2[idx]]:
            return -1

    return 0


sorted_hands = sorted(hands, key=cmp_to_key(lambda a, b: compare_hands(a[0], b[0])))

total = 0
for idx, hand in enumerate(sorted_hands):
    total += hand[1] * (idx + 1)

print(total)

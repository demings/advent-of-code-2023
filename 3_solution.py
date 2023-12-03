import functools
import re

with open("3_input.txt") as f:
    lines = f.readlines()


def get_adjacent_coords(first_digit_coord, length):
    first_x = first_digit_coord[0]
    first_y = first_digit_coord[1]

    adjacent_coords = []

    adjacent_coords.append([first_x - 1, first_y - 1])
    adjacent_coords.append([first_x - 1, first_y])
    adjacent_coords.append([first_x - 1, first_y + 1])

    for i in range(length):
        adjacent_coords.append([first_x + i, first_y - 1])
        adjacent_coords.append([first_x + i, first_y + 1])

    adjacent_coords.append([first_x + length, first_y - 1])
    adjacent_coords.append([first_x + length, first_y])
    adjacent_coords.append([first_x + length, first_y + 1])

    return adjacent_coords


for idx, line in enumerate(lines):
    lines[idx] = line.replace("\n", "")


def get_numbers_of_coords(coords, lines):
    numbers = []

    for coord in coords:
        if coord[0] < 0 or coord[1] < 0:
            continue

        if coord[0] > len(line) - 1 or coord[1] > len(lines) - 1:
            continue

        current_coords = coord.copy()
        number_str = str(lines[current_coords[1]][current_coords[0]])
        current_coords[0] -= 1
        while current_coords[0] >= 0 and lines[coord[1]][current_coords[0]].isdigit():
            for c in coords:
                if c[0] == current_coords[0] and c[1] == current_coords[1]:
                    coords.remove(c)

            number_str = lines[coord[1]][current_coords[0]] + number_str
            current_coords[0] -= 1

        current_coords[0] = coord[0] + 1
        while (
            current_coords[0] < len(lines[current_coords[1]])
            and lines[current_coords[1]][current_coords[0]].isdigit()
        ):
            for c in coords:
                if c[0] == current_coords[0] and c[1] == current_coords[1]:
                    coords.remove(c)

            number_str = number_str + lines[coord[1]][current_coords[0]]
            current_coords[0] += 1

        numbers.append(int(number_str))

    return numbers


gear_coords = []

for line_idx, line in enumerate(lines):
    for char_idx, char in enumerate(line):
        if char == "*":
            gear_coords.append([char_idx, line_idx])

multiples = []
for gear_coord in gear_coords:
    adj_coords = get_adjacent_coords(gear_coord, 1)

    digit_coords = []

    for coord in adj_coords:
        if lines[coord[1]][coord[0]].isdigit():
            digit_coords.append(coord)

    numbers = get_numbers_of_coords(digit_coords, lines)

    if len(numbers) == 2:
        multiples.append(functools.reduce(lambda a, b: a * b, numbers))

print(functools.reduce(lambda x, y: x + y, multiples))

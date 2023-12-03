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


def get_numbers_in_line(line):
    numbers = []

    for idx, char in enumerate(line):
        if char.isdigit():
            if idx > 0 and line[idx - 1].isdigit():
                numbers[len(numbers) - 1] = numbers[len(numbers) - 1] * 10 + int(char)
            else:
                numbers.append(int(char))

    return numbers


def is_symbol(char):
    return not char == "."


part_numbers = []
non_part_numbers = []

for idx, line in enumerate(lines):
    lines[idx] = line.replace("\n", "")

for line_index, line in enumerate(lines):
    numbers = get_numbers_in_line(line)

    for number in [int(num) for num in numbers]:
        number_index = line.find(str(number))

        added = False

        adj_coords = get_adjacent_coords([number_index, line_index], len(str(number)))

        for coord in adj_coords:
            if coord[0] < 0 or coord[1] < 0:
                continue

            if coord[0] > len(line) - 1 or coord[1] > len(lines) - 1:
                continue

            if is_symbol(lines[coord[1]][coord[0]]):
                part_numbers.append(number)
                added = True
                break

        if not added:
            non_part_numbers.append(number)
            line = line.replace(str(number), "X" * len(str(number)), 1)
        else:
            line = line.replace(str(number), "O" * len(str(number)), 1)

        lines[line_index] = line

print(functools.reduce(lambda x, y: x + y, part_numbers))

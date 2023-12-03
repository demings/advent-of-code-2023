with open("1_input.txt") as f:
    lines = f.readlines()

digit_map = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

calibration_sum = 0

for line in lines:
    first_digit = 0
    last_digit = 0

    current_word = ""

    for char in line:
        if char.isdigit():
            current_word = ""
            if first_digit == 0:
                first_digit = int(char)
                last_digit = int(char)
            else:
                last_digit = int(char)
        elif char.isalpha():
            current_word += char

            for digit_key in digit_map.keys():
                if current_word.endswith(digit_key):
                    if first_digit == 0:
                        first_digit = digit_map[digit_key]
                        last_digit = digit_map[digit_key]
                    else:
                        last_digit = digit_map[digit_key]
                    break

    calibration_sum += first_digit * 10 + last_digit

print(calibration_sum)

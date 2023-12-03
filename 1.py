# read lines from file 1-input.txt
with open("1-input.txt") as f:
    lines = f.readlines()

calibration_sum = 0
for line in lines:
    first_digit = 0
    last_digit = 0

    for char in line:
        if char.isdigit():
            if first_digit == 0:
                first_digit = int(char)
                last_digit = int(char)
            else:
                last_digit = int(char)

    calibration_sum += first_digit * 10 + last_digit

print(calibration_sum)

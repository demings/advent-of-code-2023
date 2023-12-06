with open("6_input.txt") as f:
    lines = f.readlines()

time = int(lines[0].split(":")[1].replace(" ", ""))
distance = int(lines[1].split(":")[1].replace(" ", ""))

nums_to_record = 0
for x in range(time):
    if (x * (time - x)) > distance:
        nums_to_record += 1

print(nums_to_record)

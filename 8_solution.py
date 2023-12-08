with open("8_input.txt") as f:
    lines = f.readlines()

instructions = lines[0].replace("\n", "")

network = {}

for line in lines[2:]:
    [key, value] = line.replace("\n", "").split(" = ")
    network[key] = value[1:-1].split(", ")

count = 0
current_key = "AAA"
current_instruction_idx = 0
while current_key != "ZZZ":
    count += 1

    current_key = network[current_key][
        0 if instructions[current_instruction_idx] == "L" else 1
    ]

    current_instruction_idx += 1
    if current_instruction_idx >= len(instructions):
        current_instruction_idx = 0

print(count)

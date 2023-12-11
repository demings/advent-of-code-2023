with open("9_input.txt") as f:
    lines = f.readlines()

first_sequences = [
    list(map(lambda x: int(x), line.replace("\n", "").split())) for line in lines
]


def get_next_sequence(sequence: list[int]):
    next_sequence = []

    for idx, el in enumerate(sequence[1:]):
        next_sequence.append(el - sequence[idx])

    return next_sequence


def get_forecast(sequences: list[list[int]]):
    last_el = 0

    for sequence in reversed(sequences):
        sequence.append(sequence[-1] + last_el)
        last_el = sequence[-1]

    return last_el


forecast_sum = 0
for first_sequence in first_sequences:
    sequences = [first_sequence]

    while any(sequences[-1]):
        sequences.append(get_next_sequence(sequences[-1]))

    forecast_sum += get_forecast(sequences)

print(forecast_sum)

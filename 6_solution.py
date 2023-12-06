with open("6_input.txt") as f:
    lines = f.readlines()

times = list(map(lambda x: int(x), lines[0].split(":")[1].strip().split())) 
distances = list(map(lambda x: int(x), lines[1].split(":")[1].strip().split()))

multiples = 1
for idx, time in enumerate(times):
    nums_to_record = 0
    for x in range(time):
        if (x * (time - x)) > distances[idx]:
            nums_to_record += 1
    if nums_to_record > 0:
        multiples *= nums_to_record

print(multiples)
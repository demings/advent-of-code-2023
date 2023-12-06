import sys, time

with open("5_input.txt") as f:
    lines = f.readlines()

seed_ranges_primitive = list(
    map(lambda x: int(x), lines[0].split("seeds: ")[1].split())
)

seed_count = 0
seed_ranges = []
for i in range(0, len(seed_ranges_primitive), 2):
    seed_ranges.append(
        range(
            seed_ranges_primitive[i],
            seed_ranges_primitive[i] + seed_ranges_primitive[i + 1],
        )
    )
    seed_count += seed_ranges_primitive[i + 1]

items = list(
    map(
        lambda x: x.strip().split("\n\n")[0].split("\n"),
        "".join(lines[2:]).split("map:")[1:],
    )
)


class MapRange:
    def __init__(self, source, destination, range_num):
        self.source = source
        self.destination = destination
        self.source_range = range(source, source + range_num)


def item_to_class(item) -> MapRange:
    elem = item.split()
    return MapRange(int(elem[1]), int(elem[0]), int(elem[2]))


seed_to_soil = list(map(lambda x: item_to_class(x), items[0]))
soil_to_fertilizer = list(map(lambda x: item_to_class(x), items[1]))
fertilizer_to_water = list(map(lambda x: item_to_class(x), items[2]))
water_to_light = list(map(lambda x: item_to_class(x), items[3]))
light_to_temperature = list(map(lambda x: item_to_class(x), items[4]))
temperature_to_humidity = list(map(lambda x: item_to_class(x), items[5]))
humidity_to_location = list(map(lambda x: item_to_class(x), items[6]))

seed_to_soil.sort(key=lambda x: x.source)
soil_to_fertilizer.sort(key=lambda x: x.source)
fertilizer_to_water.sort(key=lambda x: x.source)
water_to_light.sort(key=lambda x: x.source)
light_to_temperature.sort(key=lambda x: x.source)
temperature_to_humidity.sort(key=lambda x: x.source)
humidity_to_location.sort(key=lambda x: x.source)

def get_new_position(current_position, ranges):
    for x in ranges:
        if current_position in x.source_range:
            return current_position + (x.destination - x.source)
    return current_position


def range_overlap(range1: range, range2: range):
    x1, x2 = range1.start, range1.stop - 1
    y1, y2 = range2.start, range2.stop - 1
    return x1 <= y2 and y1 <= x2


def get_new_range(current_range, map_ranges):
    for map_range in map_ranges:
        if range_overlap(current_range, map_range.source_range):
            add_offset = True
            if current_range.stop >= map_range.source_range.stop:
                end_range = map_range.source_range.stop
            elif current_range.start >= map_range.source:
                end_range = current_range.stop
            else:
                add_offset = False
                end_range = map_range.source

            offset = (map_range.destination - map_range.source) if add_offset else 0

            return range(
                current_range.start + offset,
                end_range + offset
            )
    return current_range


print(f"Seed count: {seed_count}; current time: {time.ctime()}")

min_location = sys.maxsize
for seed_range in seed_ranges:
    i = seed_range.start
    while i < seed_range.stop:
        current_range = range(i, seed_range.stop)

        current_range = get_new_range(current_range, seed_to_soil)
        current_range = get_new_range(current_range, soil_to_fertilizer)
        current_range = get_new_range(current_range, fertilizer_to_water)
        current_range = get_new_range(current_range, water_to_light)
        current_range = get_new_range(current_range, light_to_temperature)
        current_range = get_new_range(current_range, temperature_to_humidity)
        current_range = get_new_range(current_range, humidity_to_location)

        if min_location > current_range.start:
            min_location = current_range.start
            print(
                f"Current min location: {min_location}; current time: {time.ctime()}"
            )
        
        i = i + len(current_range)

print(f"All min Location {min_location}")

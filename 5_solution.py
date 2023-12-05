with open("5_input.txt") as f:
    lines = f.readlines()

seeds = list(map(lambda x: int(x), lines[0].split("seeds: ")[1].split())) 


class MapRange:
    def __init__(self, source, destination, range):
        self.source = source
        self.destination = destination
        self.range = range


items = list(
    map(
        lambda x: x.strip().split("\n\n")[0].split("\n"),
        "".join(lines[2:]).split("map:")[1:],
    )
)


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


def get_new_position(current_position, ranges):
    for x in ranges:
        if current_position in range(x.source, x.source + x.range):
            return current_position + (x.destination - x.source)
    return current_position

locations = []
for seed in seeds:
    current_position = seed
    print(f"Seed {current_position}")

    current_position = get_new_position(current_position, seed_to_soil)
    print(f"Soil {current_position}")

    current_position = get_new_position(current_position, soil_to_fertilizer)
    print(f"Fertilizer {current_position}")

    current_position = get_new_position(current_position, fertilizer_to_water)
    print(f"Water {current_position}")

    current_position = get_new_position(current_position, water_to_light)
    print(f"Light {current_position}")

    current_position = get_new_position(current_position, light_to_temperature)
    print(f"Temperature {current_position}")

    current_position = get_new_position(current_position, temperature_to_humidity)
    print(f"Humidity {current_position}")

    current_position = get_new_position(current_position, humidity_to_location)
    print(f"Location {current_position}")

    locations.append(current_position)

print(f"Min Location {min(locations)}")
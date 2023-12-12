with open("10_input.txt") as f:
    lines = f.readlines()


class Tile:
    def __init__(self, pipe_type: str, coords: (int, int)) -> None:
        self.pipe_type = pipe_type
        self.coords = coords
        self.distance = 0


starting_coords = (0, 0)
tile_rows: list[list[Tile]] = []
for line_idx, line in enumerate(lines):
    tile_rows.append([])
    for type_idx, pipe_type in enumerate(line):
        tile_rows[line_idx].append(Tile(pipe_type, (type_idx, line_idx)))

        if pipe_type == "S":
            starting_coords = (type_idx, line_idx)


def get_possible_next_coords(coords, pipe_type):
    if pipe_type == "|":
        return [(coords[0], coords[1] + 1), (coords[0], coords[1] - 1)]

    if pipe_type == "-":
        return [(coords[0] + 1, coords[1]), (coords[0] - 1, coords[1])]

    if pipe_type == "L":
        return [(coords[0], coords[1] - 1), (coords[0] + 1, coords[1])]

    if pipe_type == "J":
        return [(coords[0], coords[1] - 1), (coords[0] - 1, coords[1])]

    if pipe_type == "7":
        return [(coords[0] - 1, coords[1]), (coords[0], coords[1] + 1)]

    if pipe_type == "F":
        return [(coords[0] + 1, coords[1]), (coords[0], coords[1] + 1)]


def get_next_coords(prev_coords, tile: Tile):
    possible_next_coords = get_possible_next_coords(tile.coords, tile.pipe_type)

    if (
        possible_next_coords[0][0] == prev_coords[0]
        and possible_next_coords[0][1] == prev_coords[1]
    ):
        return possible_next_coords[1]

    return possible_next_coords[0]


current_distance = 0
current_coords_1 = (starting_coords[0] - 1, starting_coords[1])
current_coords_2 = (starting_coords[0] + 1, starting_coords[1])
prev_coords1 = starting_coords
prev_coords2 = starting_coords
while (
    tile_rows[current_coords_1[0]][current_coords_1[1]].distance == 0
    and tile_rows[current_coords_2[0]][current_coords_2[1]].distance == 0
):
    current_distance += 1
    tile_rows[current_coords_1[0]][current_coords_1[1]].distance = current_distance
    tile_rows[current_coords_2[0]][current_coords_2[1]].distance = current_distance
    next_coords_1 = get_next_coords(
        prev_coords1, tile_rows[current_coords_1[1]][current_coords_1[0]]
    )
    next_coords_2 = get_next_coords(
        prev_coords2, tile_rows[current_coords_2[1]][current_coords_2[0]]
    )
    prev_coords1 = current_coords_1
    prev_coords2 = current_coords_2
    current_coords_1 = next_coords_1
    current_coords_2 = next_coords_2


print(current_distance)

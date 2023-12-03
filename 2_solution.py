import functools

with open("2_input.txt") as f:
    lines = f.readlines()

games = list(
    map(
        lambda x: list(
            map(
                lambda y: list(
                    map(
                        lambda z: [
                            int(z.strip().split(" ")[0]),
                            z.strip().split(" ")[1],
                        ],
                        y.split(","),
                    )
                ),
                x.split(":")[1].replace("\n", "").split(";"),
            )
        ),
        lines,
    )
)

limits = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

possible_games = []
for idx, game in enumerate(games):
    possible = True
    for sets in game:
        for set in sets:
            if set[0] > limits[set[1]]:
                possible = False
                break
        if not possible:
            break
    if possible:
        possible_games.append(idx + 1)

print(functools.reduce(lambda x, y: x + y, possible_games))

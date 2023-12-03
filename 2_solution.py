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

game_powers = []
for idx, game in enumerate(games):
    min_viable = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for sets in game:
        for set in sets:
            if set[0] > min_viable[set[1]]:
                min_viable[set[1]] = set[0]

    game_powers.append(min_viable["red"] * min_viable["green"] * min_viable["blue"])


print(functools.reduce(lambda x, y: x + y, game_powers))

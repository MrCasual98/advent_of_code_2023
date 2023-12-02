input_file = open("input.txt", "r")

max_possible_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

cumulated_ids = 0

for game in input_file:
    game_data = game.split(':')
    game_id = game_data[0].split(' ')[1]

    game_sets = game_data[1].split(';')

    max_drawn_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for game_set in game_sets:
        drawn_cubes = game_set.split(',')

        for cubes in drawn_cubes:
            cube_data = cubes.strip().split(' ')
            cube_count = cube_data[0]
            cube_color = cube_data[1]

            if max_drawn_cubes.get(cube_color) < int(cube_count):
                max_drawn_cubes.update({cube_color: int(cube_count)})

    if not any(map(lambda color: max_drawn_cubes.get(color) > max_possible_cubes.get(color), ['red', 'green', 'blue'])):
        cumulated_ids += int(game_id)



print(cumulated_ids)
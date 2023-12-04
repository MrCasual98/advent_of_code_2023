input_file = open('input.txt', 'r')

overal_points = 0

extra_cards = {}
line_number = 0

for line in input_file:
    line_numbers = line.split(':')[1]
    split_numbers = line_numbers.split('|')

    winning_numbers = [wn.strip() for wn in split_numbers[0].strip().split(' ')]
    scratch_numbers = [sn.strip() for sn in split_numbers[1].strip().split(' ')]

    matches = 0
    for scratch_number in scratch_numbers:
        if scratch_number != '' and scratch_number in winning_numbers:
            matches += 1

    repeats = 1

    if extra_cards.get(line_number) is not None:
        repeats += extra_cards.get(line_number)

    for repeat in range(repeats):
        overal_points += 1
        for match in range(matches):
            if line_number + 1 + match not in extra_cards:
                extra_cards.update({line_number + 1 + match: 1})
            else:
                extra_cards.update({line_number + 1 + match: extra_cards.get(line_number + 1 + match) + 1})

    line_number += 1

print(overal_points)

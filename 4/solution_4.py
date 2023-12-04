input_file = open('input.txt', 'r')

overal_points = 0

for line in input_file:
    line_numbers = line.split(':')[1]
    split_numbers = line_numbers.split('|')

    winning_numbers = [wn.strip() for wn in split_numbers[0].strip().split(' ')]
    scratch_numbers = [sn.strip() for sn in split_numbers[1].strip().split(' ')]

    points = 0
    for scratch_number in scratch_numbers:
        if scratch_number is not '' and scratch_number in winning_numbers:
            if points >= 1:
                points *= 2
            else:
                points = 1

    overal_points += points

print(overal_points)
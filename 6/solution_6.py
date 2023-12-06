import re

input_file = open('input.txt', 'r')

times = input_file.readline().split(':')[1].strip()
distances = input_file.readline().split(':')[1].strip()

number_pattern = re.compile("[\d]+")

times = number_pattern.findall(times)
distances = number_pattern.findall(distances)

score = 0

index = 0
for time in times:
    record_beaters = 0

    for hold_time in range(int(time)+1):
        print('Distance: ', hold_time * (int(time) - hold_time), distances[index])
        if hold_time * (int(time) - hold_time) > int(distances[index]):
            record_beaters += 1

    print(record_beaters)
    if score > 0:
        score = score * record_beaters
    else:
        score = record_beaters

    index += 1
print(score)
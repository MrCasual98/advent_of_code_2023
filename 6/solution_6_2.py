import re

input_file = open('input.txt', 'r')

times = input_file.readline().split(':')[1].strip()
distances = input_file.readline().split(':')[1].strip()

number_pattern = re.compile("[\d]+")

time = int(''.join(number_pattern.findall(times)))
distance = int(''.join(number_pattern.findall(distances)))

record_beaters = 0

for hold_time in range(time+1):
    if hold_time * (time - hold_time) > distance:
        record_beaters += 1

print(record_beaters)

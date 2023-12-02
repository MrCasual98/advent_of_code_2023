import re
import functools

input_file = open("input.txt", "r")

numbers = []

for line in input_file:
    numbers_in_line = re.findall('[0-9]', line)
    numbers.append(int(numbers_in_line[0] + numbers_in_line[-1]))

result = functools.reduce(lambda a, b: a + b, numbers)

print(result)

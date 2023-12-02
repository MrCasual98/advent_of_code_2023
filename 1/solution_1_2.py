import re
import functools

input_file = open("input.txt", "r")

number_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def map_number(number):
    return number_dict.get(number, number)


numbers = []

for line in input_file:
    numbers_in_line = re.findall('(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
    numbers.append(map_number(numbers_in_line[0]) + map_number(numbers_in_line[-1]))

result = functools.reduce(lambda a, b: int(a) + int(b), numbers)

print(result)

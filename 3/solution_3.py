import string
import re

input_file = open("input.txt", "r")


class Symbol:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol


class PartNumber:
    def __init__(self, startX, startY, number: string):
        self.startX = startX
        self.startY = startY
        self.number: string = number

    def is_adjacent(self, symbol: Symbol):
        return self.startX - 1 <= symbol.x <= self.startX + len(self.number) and self.startY - 1 <= symbol.y <= self.startY + 1


symbols = []
numbers = []
line_index = 0

for line in input_file:
    number_pattern = re.compile("[\d]+")

    for possible_part_number in number_pattern.finditer(line):
        numbers.append(PartNumber(possible_part_number.start(), line_index, possible_part_number.group()))

    symbol_pattern = re.compile("[^\d.\s]")

    for symbol in symbol_pattern.finditer(line):
        symbols.append(Symbol(symbol.start(), line_index, symbol.group()))

    line_index += 1

result = 0
result2 = 0

for number in numbers:
    if any(map(lambda symbol: number.is_adjacent(symbol), symbols)):
        result += int(number.number)
        print(number.startY, number.number)
    result2 += int(number.number)
print(result, result2)

## 529408 too high
## 525911
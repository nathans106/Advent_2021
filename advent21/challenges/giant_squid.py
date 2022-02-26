from advent21.submarine.bingo import Card, winning_score, last_score
from advent21.util.input_parser import parse_strings

lines = parse_strings('giant_squid_input.txt')

calls = [int(call) for call in lines[0].split(',')]

cards = []
matrix = []
for i in range(2, len(lines)):
    line = lines[i]
    if line == '':
        cards.append(Card(matrix))
        matrix = []
    else:
        matrix.append([int(num) for num in line.split()])

print(winning_score(cards, calls))
print(last_score(cards, calls))
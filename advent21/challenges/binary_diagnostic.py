from advent21.submarine.diagnostics import power_consumption, life_support_rating
from advent21.util.input_parser import parse_strings

report = parse_strings('binary_diagnostic_input.txt')
print(power_consumption(report))
print(life_support_rating(report))

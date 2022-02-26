from advent21.submarine.depth_rate import depth_rate, sliding_depth_rate
from advent21.util.input_parser import parse_ints

depths = parse_ints('sonar_sweep_input.txt')
rate = depth_rate(depths)
print(rate)
rate2 = sliding_depth_rate(depths)
print(rate2)

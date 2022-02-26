from advent21.submarine.navigator import AxisNavigator, execute_commands, AimingNavigator
from advent21.util.input_parser import parse_strings


def do(navigator):
    commands = parse_strings('dive_input.txt')
    execute_commands(navigator, commands)
    print(navigator.pos * navigator.depth)


do(AxisNavigator())
do(AimingNavigator())

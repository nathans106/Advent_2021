import unittest

from advent21.submarine.navigator import AxisNavigator, execute_commands, AimingNavigator


class NavigatorTests(unittest.TestCase):
    __commands = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

    def test_navigator(self):
        navigator = AxisNavigator()
        execute_commands(navigator, self.__commands)
        self.assertEqual(navigator.pos, 15)
        self.assertEqual(navigator.depth, 10)

    def test_aiming_navigator(self):
        navigator = AimingNavigator()
        execute_commands(navigator, self.__commands)
        self.assertEqual(navigator.pos, 15)
        self.assertEqual(navigator.depth, 60)

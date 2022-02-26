import unittest

from advent21.submarine.diagnostics import get_rates, oxygen_generator_rating, c02_scrubber_rating


class RatesTests(unittest.TestCase):
    __report = [
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010'
        ]

    def test_rates(self):
        gamma, epsilon = get_rates(self.__report)
        self.assertEqual(gamma, 22)
        self.assertEqual(epsilon, 9)

    def test_oxygen_generator(self):
        self.assertEqual(oxygen_generator_rating(self.__report), 23)

    def test_c02_scrubber(self):
        self.assertEqual(c02_scrubber_rating(self.__report), 10)

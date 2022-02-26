import unittest

from advent21.submarine.depth_rate import depth_rate, sliding_depth_rate


class TestDepthRate(unittest.TestCase):
    __depths = [199,200,208,210,200,207,240,269,260,263]

    def test_depth_rate(self):
        result = depth_rate(self.__depths)
        self.assertEqual(result, 7)

    def test_sliding_depth_rate(self):
        result = sliding_depth_rate(self.__depths)
        self.assertEqual(result, 5)

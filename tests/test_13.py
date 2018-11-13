import unittest
from year2018 import blackhole_13


class MyTestCase(unittest.TestCase):
    def test_13_basic_convert(self):
        self.assertEquals(blackhole_13.convert_miller_to_earth(1), 61362)

    def test_13_basic_convert_2(self):
        self.assertEquals(blackhole_13.convert_miller_to_earth(2), 122724)

if __name__ == '__main__':
    unittest.main()

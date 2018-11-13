import unittest
from year2018 import blackhole_13


class MyTestCase(unittest.TestCase):
    def test_13_basic_convert(self):
        self.assertEquals(blackhole_13.convert_miller_to_earth(1), 61362)

if __name__ == '__main__':
    unittest.main()

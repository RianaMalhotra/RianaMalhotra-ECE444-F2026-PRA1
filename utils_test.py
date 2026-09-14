import unittest
from utils import utils


class TestUtils(unittest.TestCase):

    def test_reversed_integers(self):
        self.assertEqual(utils.reversed(12345), 54321)
        self.assertEqual(utils.reversed(100), 1)
        self.assertEqual(utils.reversed(-123), -321)

    def test_reversed_strings(self):
        with self.assertRaises(TypeError):
            utils.reversed("12345")

    def test_reversed_floats(self):
        with self.assertRaises(TypeError):
            utils.reversed(123.45)

    def test_formatter_integers(self):
        self.assertEqual(utils.formatter(10), ("0b1010", "0o12"))
        self.assertEqual(utils.formatter(8), ("0b1000", "0o10"))

    def test_formatter_strings(self):
        with self.assertRaises(TypeError):
            utils.formatter("10")

    def test_formatter_floats(self):
        with self.assertRaises(TypeError):
            utils.formatter(10.5)


if __name__ == "__main__":
    unittest.main()
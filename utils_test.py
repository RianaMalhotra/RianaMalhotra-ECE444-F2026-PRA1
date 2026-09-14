import unittest
from utils import utils


class TestUtils(unittest.TestCase):

    def test_reversed_string(self):
        with self.assertRaises(TypeError):
            utils().reversed("123")

    def test_reversed_float(self):
        with self.assertRaises(TypeError):
            utils().reversed(12.5)

    def test_reversed_integer(self):
        self.assertEqual(utils().reversed(123), 321)

    def test_formatter_string(self):
        with self.assertRaises(TypeError):
            utils().formatter("10")

    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            utils().formatter(10.5)

    def test_formatter_integer(self):
        self.assertEqual(utils().formatter(10), ("0b1010", "0o12"))


if __name__ == "__main__":
    unittest.main()
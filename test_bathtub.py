import unittest

from bathtub import Bathtub


class BathtubTests(unittest.TestCase):
    """Tests for a bathtub object"""

    def setUp(self):
        self.attrs = {'colour': 'white'}

    def test_colour(self):
        """Test that raise ValueError if colour of bathtub is not a string"""
        self.attrs['colour'] = 123
        with self.assertRaises(ValueError):
            bathtub = Bathtub(**self.attrs)


if __name__ == '__main__':
    unittest.main()

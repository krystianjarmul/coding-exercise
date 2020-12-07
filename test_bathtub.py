import unittest

from bathtub import Bathtub


class BathtubTests(unittest.TestCase):
    """Tests for a bathtub object"""

    def setUp(self):
        self.attrs = {'colour': 'white',
                      'brand': 'Test',
                      'material': 'acrylic',
                      'weight': 19}

    def test_colour(self):
        """Test that raise ValueError if colour of bathtub is not a string"""
        self.attrs['colour'] = 123
        with self.assertRaises(ValueError) as e:
            Bathtub(**self.attrs)
        self.assertEqual(str(e.exception),
                         'Invalid value of colour. String required.')

    def test_brand(self):
        """Test that raise ValueError if brand of bathtub is not a string"""
        self.attrs['brand'] = []
        with self.assertRaises(ValueError) as e:
            Bathtub(**self.attrs)
        self.assertEqual(str(e.exception),
                         'Invalid value of brand. String required.')

    def test_material(self):
        """Test that raise ValueError if material of bathtub is not a string"""
        self.attrs['material'] = (1, 2)
        with self.assertRaises(ValueError):
            Bathtub(**self.attrs)

    def test_weight(self):
        """Test that raise ValueError if weight of bathtub is not a integer"""
        self.attrs['weight'] = 'test'
        with self.assertRaises(ValueError):
            Bathtub(**self.attrs)


if __name__ == '__main__':
    unittest.main()

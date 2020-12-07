import unittest

from bathtub import Bathtub


class BathtubTests(unittest.TestCase):
    """Tests for a bathtub object"""

    def setUp(self):
        self.attrs = {'colour': 'white',
                      'brand': 'Test',
                      'material': 'acrylic',
                      'weight': 19,
                      'length': 1500,
                      'width': 700,
                      'height': 400, }

    def test_colour_value_type(self):
        """Test that raise ValueError if colour of bathtub is not a string"""
        self.attrs['colour'] = 123
        with self.assertRaises(ValueError) as e:
            Bathtub(**self.attrs)
        self.assertEqual(str(e.exception),
                         'Invalid value of colour. String required.')

    def test_brand_value_type(self):
        """Test that raise ValueError if brand of bathtub is not a string"""
        self.attrs['brand'] = []
        with self.assertRaises(ValueError) as e:
            Bathtub(**self.attrs)
        self.assertEqual(str(e.exception),
                         'Invalid value of brand. String required.')

    def test_material_value_type(self):
        """Test that raise ValueError if material of bathtub is not a string"""
        self.attrs['material'] = (1, 2)
        with self.assertRaises(ValueError) as e:
            Bathtub(**self.attrs)
        self.assertEqual(str(e.exception),
                         'Invalid value of material. String required.')

    def test_weight_value_type(self):
        """Test that raise ValueError if weight of bathtub is not a integer"""
        self.attrs['weight'] = 'test'
        with self.assertRaises(ValueError) as e:
            Bathtub(**self.attrs)
        self.assertEqual(str(e.exception),
                         'Invalid value of weight. Positive integer required.')

    def test_weight_correct_value(self):
        """Test that raise ValueError if weight value is not positive"""
        self.attrs['weight'] = -5
        with self.assertRaises(ValueError) as e:
            Bathtub(**self.attrs)
            self.attrs['weight'] = 0
            Bathtub(**self.attrs)
        self.assertEqual(str(e.exception),
                         'Invalid value of weight. Positive integer required.')

    def test_length_value_type(self):
        """Test that raise ValueError if length of bathtub is not a integer"""
        self.attrs['length'] = ''
        with self.assertRaises(ValueError) as e:
            Bathtub(**self.attrs)
        self.assertEqual(str(e.exception),
                         'Invalid value of length. Positive integer required.')

    def test_length_correct_value(self):
        """Test that raise ValueError if length value is not positive"""
        self.attrs['length'] = 0
        with self.assertRaises(ValueError) as e:
            Bathtub(**self.attrs)
            self.attrs['length'] = -13
            Bathtub(**self.attrs)
        self.assertEqual(str(e.exception),
                         'Invalid value of length. Positive integer required.')

    def test_width_value_type(self):
        """Test that raise ValueError if width of bathtub is not a integer"""
        self.attrs['width'] = ''
        with self.assertRaises(ValueError) as e:
            Bathtub(**self.attrs)
        self.assertEqual(str(e.exception),
                         'Invalid value of width. Positive integer required.')

    def test_width_correct_value(self):
        """Test that raise ValueError if width value is not positive"""
        self.attrs['width'] = 0
        with self.assertRaises(ValueError) as e:
            Bathtub(**self.attrs)
            self.attrs['width'] = -13
            Bathtub(**self.attrs)
        self.assertEqual(str(e.exception),
                         'Invalid value of width. Positive integer required.')

    def test_height_value_type(self):
        """Test that raise ValueError if height of bathtub is not a integer"""
        self.attrs['height'] = ['test']
        with self.assertRaises(ValueError) as e:
            Bathtub(**self.attrs)
        self.assertEqual(str(e.exception),
                         'Invalid value of height. Positive integer required.')

    def test_height_correct_value(self):
        """Test that raise ValueError if height value is not positive"""
        self.attrs['height'] = 0
        with self.assertRaises(ValueError) as e:
            Bathtub(**self.attrs)
            self.attrs['height'] = -3
            Bathtub(**self.attrs)
        self.assertEqual(str(e.exception),
                         'Invalid value of height. Positive integer required.')


if __name__ == '__main__':
    unittest.main()

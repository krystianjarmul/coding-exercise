import unittest
from unittest import mock

from bathtub import Bathtub, BathtubError


class BathtubTests(unittest.TestCase):
    """Tests for a bathtub object"""

    def setUp(self):
        self.attrs = {'colour': 'white',
                      'brand': 'Test',
                      'material': 'acrylic',
                      'weight': 19,
                      'length': 1500,
                      'width': 700,
                      'height': 400,
                      'capacity': 180}
        self.bathtub = Bathtub(**self.attrs)

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
        """Test that raise ValueError if weight of bathtub is not an integer"""
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
        """Test that raise ValueError if length of bathtub is not an integer"""
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
        """Test that raise ValueError if width of bathtub is not an integer"""
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
        """Test that raise ValueError if height of bathtub is not an integer"""
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

    def test_capacity_value_type(self):
        """Test that raise ValueError if capacity of bathtub isn't an integer"""
        self.attrs['capacity'] = (180,)

        with self.assertRaises(ValueError) as e:
            Bathtub(**self.attrs)

        self.assertEqual(str(e.exception),
                         'Invalid value of capacity. Positive integer required.')

    def test_capacity_correct_value(self):
        """Test that raise ValueError if capacity value is not positive"""
        self.attrs['capacity'] = 0

        with self.assertRaises(ValueError) as e:
            Bathtub(**self.attrs)
            self.attrs['capacity'] = -3
            Bathtub(**self.attrs)

        self.assertEqual(str(e.exception),
                         'Invalid value of capacity. Positive integer required.')

    def test_put_stopper_successfully(self):
        """Test putting a stopper to the bathtub when it's empty"""
        self.bathtub.put_stopper()

        self.assertTrue(self.bathtub.has_stopper_in)

    def test_put_stopper_already_in(self):
        """Test putting a stopper raise BathtubError when it's already in"""
        self.bathtub.has_stopper_in = True

        with self.assertRaises(BathtubError) as e:
            self.bathtub.put_stopper()

        self.assertEqual(str(e.exception), 'Stopper is already in.')

    def test_fill_without_stopper(self):
        """Test running a bath raise BathtubError if stopper is not inserted"""
        with self.assertRaises(BathtubError) as e:
            self.bathtub.fill()

        self.assertEqual(str(e.exception), 'Stopper is not inserted.')

    def test_fill_successfully(self):
        """Test running a bath with stopper is successful"""
        self.bathtub.put_stopper()

        self.bathtub.fill()

        self.assertTrue(self.bathtub.is_filled)

    @mock.patch('builtins.print')
    def test_use_bathtub_successfully(self, bath_mock):
        """Test taking a bath"""
        self.bathtub.put_stopper()
        self.bathtub.fill()

        self.bathtub.use()

        bath_mock.assert_called_once()

    def test_use_bathtub_unsuccessfully(self):
        """Test taking a bath raise BathtubError if a bathtub is not filled"""
        with self.assertRaises(BathtubError) as e:
            self.bathtub.use()

        self.assertEqual(str(e.exception), 'Bathtub is not filled.')


if __name__ == '__main__':
    unittest.main()

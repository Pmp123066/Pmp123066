import unittest

from src.converter import convert


class TestLengthConversions(unittest.TestCase):
    def test_km_to_miles(self):
        result = convert(1, "kilometers", "miles", "length")
        self.assertAlmostEqual(result, 0.621371, places=4)

    def test_miles_to_km(self):
        result = convert(1, "miles", "kilometers", "length")
        self.assertAlmostEqual(result, 1.60934, places=4)

    def test_feet_to_meters(self):
        result = convert(1, "feet", "meters", "length")
        self.assertAlmostEqual(result, 0.3048, places=4)

    def test_inches_to_centimeters(self):
        result = convert(1, "inches", "centimeters", "length")
        self.assertAlmostEqual(result, 2.54, places=2)

    def test_same_unit(self):
        self.assertEqual(convert(42, "meters", "meters", "length"), 42)

    def test_round_trip(self):
        original = 5.0
        miles = convert(original, "kilometers", "miles", "length")
        back = convert(miles, "miles", "kilometers", "length")
        self.assertAlmostEqual(back, original, places=6)


class TestWeightConversions(unittest.TestCase):
    def test_pounds_to_kilograms(self):
        result = convert(1, "pounds", "kilograms", "weight")
        self.assertAlmostEqual(result, 0.453592, places=4)

    def test_kilograms_to_pounds(self):
        result = convert(1, "kilograms", "pounds", "weight")
        self.assertAlmostEqual(result, 2.20462, places=4)

    def test_ounces_to_grams(self):
        result = convert(1, "ounces", "grams", "weight")
        self.assertAlmostEqual(result, 28.3495, places=2)

    def test_same_unit(self):
        self.assertEqual(convert(100, "grams", "grams", "weight"), 100)


class TestTemperatureConversions(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(convert(0, "celsius", "fahrenheit", "temperature"), 32)
        self.assertAlmostEqual(convert(100, "celsius", "fahrenheit", "temperature"), 212)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(convert(32, "fahrenheit", "celsius", "temperature"), 0)
        self.assertAlmostEqual(convert(212, "fahrenheit", "celsius", "temperature"), 100)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(convert(0, "celsius", "kelvin", "temperature"), 273.15)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(convert(273.15, "kelvin", "celsius", "temperature"), 0)

    def test_fahrenheit_to_kelvin(self):
        result = convert(32, "fahrenheit", "kelvin", "temperature")
        self.assertAlmostEqual(result, 273.15)

    def test_same_unit(self):
        self.assertEqual(convert(37, "celsius", "celsius", "temperature"), 37)

    def test_negative_temperature(self):
        result = convert(-40, "celsius", "fahrenheit", "temperature")
        self.assertAlmostEqual(result, -40)

    def test_absolute_zero(self):
        result = convert(0, "kelvin", "celsius", "temperature")
        self.assertAlmostEqual(result, -273.15)


class TestEdgeCases(unittest.TestCase):
    def test_zero_value(self):
        self.assertEqual(convert(0, "miles", "kilometers", "length"), 0)

    def test_unknown_category(self):
        with self.assertRaises(ValueError):
            convert(1, "foo", "bar", "unknown")


if __name__ == "__main__":
    unittest.main()

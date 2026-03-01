import unittest

from src.tax import calculate_tax, calculate_pretax, PRESET_TAX_RATES


class TestCalculateTax(unittest.TestCase):
    def test_basic_tax(self):
        result = calculate_tax(100, 7.25)
        self.assertEqual(result["subtotal"], 100.00)
        self.assertEqual(result["tax_amount"], 7.25)
        self.assertEqual(result["total"], 107.25)

    def test_zero_rate(self):
        result = calculate_tax(50, 0)
        self.assertEqual(result["tax_amount"], 0)
        self.assertEqual(result["total"], 50)

    def test_zero_subtotal(self):
        result = calculate_tax(0, 8.5)
        self.assertEqual(result["tax_amount"], 0)
        self.assertEqual(result["total"], 0)

    def test_rounding(self):
        # $19.99 at 7.25% = $1.449275 -> rounds to $1.45
        result = calculate_tax(19.99, 7.25)
        self.assertEqual(result["tax_amount"], 1.45)
        self.assertEqual(result["total"], 21.44)

    def test_negative_subtotal_raises(self):
        with self.assertRaises(ValueError):
            calculate_tax(-10, 5)

    def test_negative_rate_raises(self):
        with self.assertRaises(ValueError):
            calculate_tax(100, -5)

    def test_large_amount(self):
        result = calculate_tax(9999.99, 10)
        self.assertEqual(result["tax_amount"], 1000.00)
        self.assertEqual(result["total"], 10999.99)


class TestCalculatePretax(unittest.TestCase):
    def test_basic_reverse(self):
        result = calculate_pretax(107.25, 7.25)
        self.assertEqual(result["subtotal"], 100.00)
        self.assertEqual(result["total"], 107.25)

    def test_zero_rate(self):
        result = calculate_pretax(50, 0)
        self.assertEqual(result["subtotal"], 50)
        self.assertEqual(result["tax_amount"], 0)

    def test_zero_total(self):
        result = calculate_pretax(0, 8.5)
        self.assertEqual(result["subtotal"], 0)
        self.assertEqual(result["tax_amount"], 0)

    def test_negative_total_raises(self):
        with self.assertRaises(ValueError):
            calculate_pretax(-10, 5)

    def test_negative_rate_raises(self):
        with self.assertRaises(ValueError):
            calculate_pretax(100, -5)

    def test_round_trip(self):
        # Calculate tax, then reverse it — should get back close to original
        forward = calculate_tax(49.99, 6.25)
        reverse = calculate_pretax(forward["total"], 6.25)
        self.assertAlmostEqual(reverse["subtotal"], 49.99, places=2)


class TestPresetRates(unittest.TestCase):
    def test_presets_are_non_negative(self):
        for state, rate in PRESET_TAX_RATES.items():
            self.assertGreaterEqual(rate, 0, f"{state} has negative rate")

    def test_presets_are_reasonable(self):
        for state, rate in PRESET_TAX_RATES.items():
            self.assertLessEqual(rate, 15, f"{state} rate seems too high: {rate}%")


if __name__ == "__main__":
    unittest.main()

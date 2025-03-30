import unittest
from src.utils.uiSupport import rgba_to_hex

class TestUiSupport(unittest.TestCase):

    def test_rgba_to_hex(self):
        # Test cases: (R, G, B, A) -> Expected Hex
        test_cases = [
            ((173, 216, 230), "#add8e6"),   # Light blue
            ((255, 0, 0), "#ff0000"),       # Red
            ((0, 255, 0), "#00ff00"),       # Green
            ((0, 0, 255), "#0000ff"),       # Blue
            ((0, 0, 0), "#000000"),         # Black
            ((255, 255, 255), "#ffffff")    # White
        ]

        for (r, g, b), expected in test_cases:
            with self.subTest(r=r, g=g, b=b):
                result = rgba_to_hex(r, g, b)
                self.assertEqual(result, expected, f"Failed for rgba({r}, {g}, {b})")

    def test_invalid_values(self):
        # Test invalid input (values out of range)
        with self.assertRaises(ValueError):
            rgba_to_hex(-1, 0, 0)  # Negative red value
        with self.assertRaises(ValueError):
            rgba_to_hex(256, 0, 0) # Red value out of range
        with self.assertRaises(ValueError):
            rgba_to_hex(0, 300, 0) # Green value out of range
        with self.assertRaises(ValueError):
            rgba_to_hex(0, 0, 999) # Blue value out of range

if __name__ == '__main__':
    unittest.main()

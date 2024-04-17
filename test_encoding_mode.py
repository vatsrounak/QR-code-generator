import unittest
from encoding_mode import determine_encoding_mode

class TestEncodingMode(unittest.TestCase):
    def test_numeric_mode(self):
        self.assertEqual(determine_encoding_mode("1234567890"), "numeric")
        self.assertNotEqual(determine_encoding_mode("1234ABC567890"), "numeric")
        self.assertNotEqual(determine_encoding_mode("12!34@567890"), "numeric")

    def test_alphanumeric_mode(self):
        self.assertEqual(determine_encoding_mode("ABC123DEF456"), "alphanumeric")
        self.assertNotEqual(determine_encoding_mode("ABC123DEF!456"), "alphanumeric")
        self.assertNotEqual(determine_encoding_mode("ABC123DEF&456"), "alphanumeric")

    def test_byte_mode(self):
        self.assertEqual(determine_encoding_mode("Hello World"), "byte")
        self.assertEqual(determine_encoding_mode("Hello$World!"), "byte")
        self.assertNotEqual(determine_encoding_mode("Hello123World"), "byte")

    def test_kanji_mode(self):
        self.assertEqual(determine_encoding_mode("こんにちは、世界"), "kanji")
        self.assertNotEqual(determine_encoding_mode("こんにちは、World"), "kanji")
        self.assertNotEqual(determine_encoding_mode("Helloこんにちは"), "kanji")

    def test_invalid_cases(self):
        self.assertIsNone(determine_encoding_mode(""))
        self.assertIsNone(determine_encoding_mode(None))

if __name__ == "__main__":
    unittest.main()      
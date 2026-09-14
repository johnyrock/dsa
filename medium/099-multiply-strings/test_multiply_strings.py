import unittest
from multiply_strings import Solution


class TestMultiplyStrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_multiply(self):
        cases = [
            # (num1, num2, expected)
            ("123", "456", "56088"),        # the running example in the walkthrough
            ("2", "3", "6"),                # single digits, the leading cell stays 0 and is stripped
            ("99", "99", "9801"),           # every partial product carries
            ("0", "12345", "0"),            # zero factor must give "0", not "000000"
            ("12345", "0", "0"),
            ("1", "1", "1"),
            ("9", "9", "81"),               # uses both cells of a 2-cell result
            ("100", "100", "10000"),        # trailing zeros in both inputs
            ("123456789", "987654321", "121932631112635269"),   # far beyond 64-bit precision territory later on
            ("9" * 200, "9" * 200, str((10 ** 200 - 1) ** 2)),  # constraint maximum: 200-digit inputs
        ]

        for num1, num2, expected in cases:
            with self.subTest(num1=num1, num2=num2):
                result = self.solution.multiply(num1, num2)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

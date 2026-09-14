import unittest
from encode_and_decode_strings import Solution


class TestEncodeAndDecodeStrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_round_trip(self):
        cases = [
            # (strs)
            ["neet", "code", "love", "you"],   # the running example in the walkthrough
            ["we", "say", ":", "yes"],
            [],                                 # empty list encodes to "" and decodes back to []
            [""],                               # a single empty string must survive as one element
            ["", "", ""],                       # several empties must keep their count
            ["#", "1#", "#2#"],                 # the delimiter appears inside the payloads
            ["12#34", "5"],                     # digits followed by '#' inside a payload
            ["a" * 123, "b"],                   # a multi-digit length header
            ["héllo", "日本語"],                 # non-ASCII characters
        ]

        for strs in cases:
            with self.subTest(strs=strs):
                encoded = self.solution.encode(strs)
                self.assertIsInstance(encoded, str)
                self.assertEqual(self.solution.decode(encoded), strs)

    def test_encoding_shape(self):
        # the exact format is not required, but the walkthrough relies on this one
        self.assertEqual(self.solution.encode(["neet", "code", "love", "you"]), "4#neet4#code4#love3#you")
        self.assertEqual(self.solution.encode([""]), "0#")
        self.assertEqual(self.solution.encode([]), "")


if __name__ == '__main__':
    unittest.main()

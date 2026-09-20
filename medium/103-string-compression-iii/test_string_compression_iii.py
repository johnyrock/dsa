import unittest
from string_compression_iii import Solution


class TestStringCompressionIII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_compressed_string(self):
        cases = [
            # (word, expected)
            ("aabbdd", "2a2b2d"),
            ("abcde", "1a1b1c1d1e"),               # every run has length 1, so every count is 1
            ("aaaaaaaaaaaaaabb", "9a5a2b"),        # 14 a's split into 9 + 5
            ("a", "1a"),                           # shortest input
            ("aaaaaaaaa", "9a"),                   # exactly 9, one piece
            ("aaaaaaaaaa", "9a1a"),                # 10 = 9 + 1, the second piece has count 1
            ("aaaaaaaaaaaaaaaaaa", "9a9a"),        # 18 = 9 + 9
            ("z" * 27, "9z9z9z"),                  # 27 = three full pieces
            ("z" * 28, "9z9z9z1z"),                # 28 = three full pieces plus a leftover of 1
            ("abab", "1a1b1a1b"),                  # runs are contiguous, so a and b are not merged
            ("aab", "2a1b"),                       # last run has length 1
            ("baa", "1b2a"),                       # first run has length 1
        ]

        for word, expected in cases:
            with self.subTest(word=word):
                self.assertEqual(self.solution.compressed_string(word), expected)


if __name__ == '__main__':
    unittest.main()

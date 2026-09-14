import unittest
from detect_squares import DetectSquares


def run(ops):
    # ops is a list of ("add", [x, y]) or ("count", [x, y]); returns the results of count in order
    squares = DetectSquares()
    out = []
    for op, point in ops:
        if op == "add":
            squares.add(point)
        else:
            out.append(squares.count(point))
    return out


class TestDetectSquares(unittest.TestCase):
    def test_detect_squares(self):
        cases = [
            # (ops, expected results of count)
            ([("add", [3, 10]), ("add", [11, 2]), ("add", [3, 2]), ("count", [11, 10]), ("count", [14, 8]), ("add", [11, 2]), ("count", [11, 10])], [1, 0, 2]),   # the running example in the walkthrough
            ([("count", [0, 0])], [0]),                                                                       # nothing stored yet
            ([("add", [0, 0]), ("add", [1, 1]), ("add", [0, 1]), ("count", [1, 0])], [1]),                   # unit square, query at the bottom-right corner
            ([("add", [0, 0]), ("add", [2, 2]), ("add", [0, 2]), ("count", [2, 0])], [1]),                   # side 2
            ([("add", [0, 0]), ("add", [2, 0]), ("add", [0, 2]), ("count", [2, 2])], [1]),                   # query is the top-right corner
            ([("add", [0, 0]), ("add", [1, 2]), ("add", [0, 2]), ("count", [1, 0])], [0]),                   # dx = 1, dy = 2: a rectangle, not a square
            ([("add", [1, 1]), ("add", [1, 3]), ("add", [3, 1]), ("add", [3, 3]), ("count", [1, 1])], [1]),  # the query point itself is stored; a stored copy is not reused as the query
            ([("add", [0, 0]), ("add", [0, 0]), ("add", [1, 1]), ("add", [0, 1]), ("count", [1, 0])], [2]),  # duplicate diagonal corner doubles the count
            ([("add", [0, 0]), ("add", [1, 1]), ("add", [1, 1]), ("add", [0, 1]), ("add", [0, 1]), ("count", [1, 0])], [4]),   # 1 * 2 * 2 copies
            ([("add", [1, 0]), ("add", [0, 1]), ("add", [1, 1]), ("add", [-1, 1]), ("add", [-1, 0]), ("count", [0, 0])], [2]),  # two squares on either side of the query (negative x only for the test)
            ([("add", [0, 0]), ("add", [0, 5]), ("add", [5, 0]), ("count", [5, 5]), ("count", [0, 0])], [1, 0]),   # (0,0) as query: diagonal (5,5) is missing
        ]

        for ops, expected in cases:
            with self.subTest(ops=ops):
                result = run(ops)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

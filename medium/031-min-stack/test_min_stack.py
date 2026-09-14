import unittest
from min_stack import MinStack


def run(ops):
    # ops is a list of ("push", val), ("pop",), ("top",) or ("get_min",); returns the results of top/get_min in order
    stack = MinStack()
    out = []
    for op in ops:
        if op[0] == "push":
            stack.push(op[1])
        elif op[0] == "pop":
            stack.pop()
        elif op[0] == "top":
            out.append(stack.top())
        else:
            out.append(stack.get_min())
    return out


class TestMinStack(unittest.TestCase):
    def test_min_stack(self):
        cases = [
            # (ops, expected results of top / get_min)
            ([("push", -2), ("push", 0), ("push", -3), ("get_min",), ("pop",), ("top",), ("get_min",)], [-3, 0, -2]),   # the running example in the walkthrough
            ([("push", 5), ("get_min",), ("top",)], [5, 5]),                                       # single element is both top and min
            ([("push", 3), ("push", 1), ("push", 2), ("get_min",), ("pop",), ("get_min",), ("pop",), ("get_min",)], [1, 1, 3]),   # popping a non-min leaves the min alone
            ([("push", 1), ("push", 1), ("pop",), ("get_min",)], [1]),                             # duplicate minimum: strict < on push would break this
            ([("push", 2), ("push", 2), ("push", 1), ("pop",), ("pop",), ("get_min",), ("top",)], [2, 2]),
            ([("push", 4), ("push", 3), ("push", 2), ("push", 1), ("pop",), ("pop",), ("get_min",)], [3]),   # strictly decreasing pushes, min_stack mirrors stack
            ([("push", 1), ("push", 2), ("push", 3), ("get_min",), ("pop",), ("pop",), ("get_min",)], [1, 1]),   # strictly increasing pushes, min_stack has one entry
            ([("push", -2**31), ("push", 2**31 - 1), ("get_min",), ("top",)], [-2**31, 2**31 - 1]),   # constraint extremes
            ([("push", 0), ("push", -1), ("push", 0), ("pop",), ("get_min",), ("pop",), ("get_min",)], [-1, 0]),   # min resurfaces after the -1 is popped
        ]

        for ops, expected in cases:
            with self.subTest(ops=ops):
                result = run(ops)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

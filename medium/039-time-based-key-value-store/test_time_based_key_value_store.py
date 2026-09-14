import unittest
from time_based_key_value_store import TimeMap


def run(ops):
    # ops is a list of ("set", key, value, timestamp) or ("get", key, timestamp); returns the list of get results
    store = TimeMap()
    out = []
    for op in ops:
        if op[0] == "set":
            store.set(op[1], op[2], op[3])
        else:
            out.append(store.get(op[1], op[2]))
    return out


class TestTimeBasedKeyValueStore(unittest.TestCase):
    def test_time_map(self):
        cases = [
            # (ops, expected get results)
            ([("set", "foo", "bar", 1), ("set", "foo", "bar2", 4), ("set", "foo", "bar3", 7),
              ("get", "foo", 4), ("get", "foo", 5), ("get", "foo", 0), ("get", "foo", 9)],
             ["bar2", "bar2", "", "bar3"]),                                          # the running example in the walkthrough
            ([("set", "foo", "bar", 1), ("get", "foo", 1), ("get", "foo", 3), ("set", "foo", "bar2", 4),
              ("get", "foo", 4), ("get", "foo", 5)], ["bar", "bar", "bar2", "bar2"]),  # LeetCode's example
            ([("get", "missing", 5)], [""]),                                          # key never set
            ([("set", "a", "x", 10), ("get", "a", 9)], [""]),                          # every write is newer than asked
            ([("set", "a", "x", 10), ("get", "a", 10)], ["x"]),                        # exact timestamp match must count
            ([("set", "a", "x", 1), ("set", "a", "y", 2), ("set", "a", "z", 3),
              ("get", "a", 3), ("get", "a", 2), ("get", "a", 1), ("get", "a", 100)], ["z", "y", "x", "z"]),
            ([("set", "a", "x", 5), ("set", "b", "y", 5), ("get", "a", 5), ("get", "b", 5), ("get", "b", 4)],
             ["x", "y", ""]),                                                        # keys keep separate histories
            ([("set", "love", "high", 10), ("set", "love", "low", 20), ("get", "love", 5), ("get", "love", 10),
              ("get", "love", 15), ("get", "love", 20), ("get", "love", 25)], ["", "high", "high", "low", "low"]),
        ]

        for ops, expected in cases:
            with self.subTest(ops=ops):
                result = run(ops)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

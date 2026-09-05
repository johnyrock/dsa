from two_sum import two_sum


def test_example_1():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_example_2():
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_duplicate_values():
    # Two 3s: must use both indices, not the same one twice.
    assert two_sum([3, 3], 6) == [0, 1]


def test_negative_numbers():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]


def test_zero_target():
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]


def test_minimum_length():
    assert two_sum([1, 5], 6) == [0, 1]


def test_does_not_pair_element_with_itself():
    # 4 + 4 = 8 but there is only one 4, so [0, 0] is wrong.
    assert two_sum([4, 1, 7], 8) == [1, 2]


def test_no_answer_returns_empty():
    assert two_sum([1, 2, 3], 100) == []

import pytest

from two_sum import two_sum


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),            # duplicate values, must not reuse one index
        ([-1, -2, -3, -4, -5], -8, [2, 4]),  # negatives
        ([0, 4, 3, 0], 0, [0, 3]),      # zero target
        ([1, 5], 6, [0, 1]),            # minimum length
    ],
)
def test_two_sum(nums, target, expected):
    assert two_sum(nums, target) == expected


def test_does_not_pair_element_with_itself():
    # 4 + 4 = 8 but there is only one 4; must not return [0, 0]
    assert two_sum([4, 1, 7], 8) == [1, 2]


def test_no_answer_returns_empty():
    assert two_sum([1, 2, 3], 100) == []

import pytest

from slug import solve


@pytest.mark.parametrize(
    "args, expected",
    [
        # (( ...inputs ), expected),
    ],
)
def test_solve(args, expected):
    assert solve(*args) == expected

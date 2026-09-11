from two_sum import two_sum

cases = [
    #nums, target, expected
    ([7,11,8,5],13,[2,3])
]

def test_two_sum(cases):
    for nums, target, expected in cases:
        result = two_sum(nums, target)
        assert result == expected, f'{nums} -> FAIL. result={result}, expected={expected}'
        print(f'{nums} -> PASS. result={result}, expected={expected}')


test_two_sum(cases)
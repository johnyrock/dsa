# s=[7,2,11,16], target=9, expected=[0,1]

def two_sum(s, t):
    seen = {}
    for i, n in enumerate(s):
        # print(f'{i}, {n}')
        complement = t - n
        # print(f'{seen.get(complement)}')
        if complement in seen:
            # return f'FOUND: {seen[complement]}, {i}'
            # return f'FOUND: {seen.get(complement)}, {i}'
            return [seen.get(complement), i]
        seen[n] = i
    return []

print(two_sum([7,2,11,16], 13))
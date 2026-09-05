def contains_duplicate(nums):
    seen = set()  # values already visited
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

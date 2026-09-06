# Define the function that takes the array and returns every distinct triplet summing to zero.
def three_sum(nums):
    # Sorting is what makes both tricks below work: two pointers need order, and duplicates become neighbours.
    nums.sort()
    result = []
    n = len(nums)
    # Fix the first number of the triplet. It only needs to run up to n - 3, leaving room for two more.
    for i in range(n - 2):
        # Sorted, so if the smallest of the three is positive the sum can never reach zero. Stop early.
        if nums[i] > 0:
            break  # everything after is positive too, no zero sum possible
        # If this first value equals the previous first value, every triplet it can form was already found.
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # same first value as before, would repeat triplets
        # Two Sum on the rest of the array, with the target -nums[i], done with two pointers closing inward.
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                # Too small: the only way to grow the sum is to move the left pointer to a bigger number.
                left += 1
            elif total > 0:
                # Too big: shrink by moving the right pointer to a smaller number.
                right -= 1
            else:
                # Exactly zero. Record the triplet, then move both pointers, because neither current value can pair with anything else to hit zero with this nums[i].
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip over any copies of the second value, or the same triplet would be recorded again.
                while left < right and nums[left] == nums[left - 1]:
                    left += 1  # skip duplicate second values
    return result

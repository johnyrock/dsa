# Define the function that takes a sorted list of integers and the value we are hunting for.
def search(nums, target):
    # Set up the search window as the whole array: lo is the first index we still consider, hi is the last one. Using len(nums) - 1 makes hi an index that really exists, not one past the end.
    lo, hi = 0, len(nums) - 1
    # Keep going while the window still holds at least one element. The <= matters: when lo == hi there is exactly one candidate left, and it still has to be checked.
    while lo <= hi:
        # Pick the middle index of the current window. Integer division floors, so mid leans left when the window has an even number of elements.
        mid = (lo + hi) // 2
        # Compare the middle value with the target first, because that is the only case where we can stop early.
        if nums[mid] == target:
            # The middle element is the answer, and the problem asks for the index, so return mid itself.
            return mid
        # If the middle value is too small, everything from lo through mid is too small as well, because the array is sorted.
        if nums[mid] < target:
            # Throw that whole left half away by moving lo past mid. The + 1 is what guarantees the window shrinks, so the loop cannot spin forever.
            lo = mid + 1
        # Otherwise the middle value is too big, so the target cannot be at mid or anywhere to its right.
        else:
            # Throw the right half away by moving hi below mid. The - 1 excludes mid, which we already know is not the answer.
            hi = mid - 1
    # The loop only ends when lo passes hi, meaning the window is empty and the target is not in the array.
    return -1

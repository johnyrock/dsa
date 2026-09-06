def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        area = (right - left) * min(height[left], height[right])
        if area > best:
            best = area
        if height[left] < height[right]:
            left += 1   # the shorter line is the limit; only moving it can help
        else:
            right -= 1
    return best

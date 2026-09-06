# Define the function that takes the line heights and returns the largest area any two lines can enclose.
def max_area(height):
    # Start with the widest possible container: the two outermost lines.
    left, right = 0, len(height) - 1
    best = 0
    # Each iteration moves one pointer inward, so the loop runs at most n - 1 times.
    while left < right:
        # Area is width times the shorter of the two lines; the taller one cannot hold water above the shorter one.
        area = (right - left) * min(height[left], height[right])
        if area > best:
            best = area
        # Moving either pointer shrinks the width. If we move the taller line, the height is still capped by the shorter one, so the area can only go down. Moving the shorter line is the only move that might find a taller wall and a bigger area.
        if height[left] < height[right]:
            left += 1   # the shorter line is the limit; only moving it can help
        else:
            # Ties go either way; moving right is fine because the left line is just as limiting.
            right -= 1
    # Every pair that could beat the running best was examined, so best is the answer.
    return best

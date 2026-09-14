class Solution:
    # Take the jump lengths and return the fewest jumps from index 0 to the last index (a solution is guaranteed to exist).
    def jump(self, nums: list[int]) -> int:
        # Number of jumps committed so far.
        jumps = 0
        # Right edge of the window the current number of jumps can reach. With zero jumps we can only stand on index 0.
        end = 0
        # Farthest index reachable by taking one more jump from anywhere inside the current window.
        farthest = 0
        # Stop before the last index: once we are standing on it no further jump is needed, and visiting it would count a phantom jump.
        for i in range(len(nums) - 1):
            # Every index inside the window is a candidate launch point; remember the best landing spot any of them offers.
            farthest = max(farthest, i + nums[i])
            # Reaching the window's right edge means the next index needs one more jump; commit it and open the next window.
            if i == end:
                jumps += 1
                # The new window spans everything reachable with that extra jump. This is BFS by levels without a queue.
                end = farthest
        # The last index sits inside the final window, so jumps is the level it was discovered on.
        return jumps

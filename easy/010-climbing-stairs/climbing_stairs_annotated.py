# Define the function that takes the number of stairs and returns how many distinct ways there are to climb them.
def climb_stairs(n):
    # Handle the two base cases up front: 1 stair has 1 way, 2 stairs have 2 ways (1+1 or 2).
    if n <= 2:
        # For n = 1 and n = 2 the answer happens to equal n itself, so return it directly.
        return n
    # Seed the two rolling variables with those base cases. Nothing else from the table is ever needed, because each answer depends only on the previous two.
    two_back, one_back = 1, 2  # ways to reach step 1 and step 2
    # Walk the steps from 3 up to n. Starting at 3 matters: steps 1 and 2 are already accounted for by the seed values.
    for _ in range(3, n + 1):
        # Slide the window one step up. The new count is the sum of the previous two, and the old one_back becomes the new two_back. The tuple assignment reads the right-hand side before rebinding either name, so no temporary variable is needed.
        two_back, one_back = one_back, two_back + one_back
    # After the last iteration one_back holds the count for step n, which is the answer.
    return one_back

from hand_of_straights import Solution

solution = Solution()

for hand, group_size in (([1, 2, 3, 6, 2, 3, 4, 7, 8], 3), ([1, 2, 3, 4, 5], 4), ([1, 1, 2, 2, 3, 3], 3)):
    print(hand, group_size, solution.is_n_straight_hand(hand, group_size))

from collections import Counter


class Solution:
    # Take the cards and the group size; report whether the hand splits into groups of group_size consecutive cards.
    def is_n_straight_hand(self, hand: list[int], group_size: int) -> bool:
        # Every card must belong to exactly one group, so the total has to divide evenly. Cheap early exit.
        if len(hand) % group_size:
            return False
        # How many copies of each value we still have to place.
        count = Counter(hand)
        # Visit values from smallest to largest. The smallest unplaced card has no smaller neighbour, so it can only ever be the *start* of a group; there is no choice to make.
        for card in sorted(count):
            # All remaining copies of this value must start their own groups, so we open `need` groups at once.
            need = count[card]
            # A value already used up by earlier groups (as a middle or end card) starts nothing.
            if need:
                # Each of those groups needs card, card + 1, ..., card + group_size - 1.
                for c in range(card, card + group_size):
                    # Not enough copies of a required value means at least one group cannot be completed, and no other arrangement can rescue it.
                    if count[c] < need:
                        return False
                    # Consume `need` copies of this value, one per group being opened.
                    count[c] -= need
        # Every value was placed, so the grouping exists.
        return True

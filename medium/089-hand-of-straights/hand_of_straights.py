from collections import Counter


class Solution:
    def is_n_straight_hand(self, hand: list[int], group_size: int) -> bool:
        if len(hand) % group_size:
            return False
        count = Counter(hand)
        for card in sorted(count):
            need = count[card]
            if need:
                for c in range(card, card + group_size):
                    if count[c] < need:
                        return False
                    count[c] -= need
        return True

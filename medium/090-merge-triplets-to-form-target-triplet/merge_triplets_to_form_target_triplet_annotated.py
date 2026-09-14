class Solution:
    # Decide whether some subset of the triplets, merged with element-wise max, equals target.
    def merge_triplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        # Which of the three positions have we already matched exactly with a safe triplet? Merging is a max, so once a position hits target it never drops back down.
        found = set()
        # Look at every triplet once; order does not matter because max is commutative.
        for triplet in triplets:
            # A triplet is safe to include only if it never exceeds target in any position. One value above target would poison the max forever, so such a triplet must be skipped entirely.
            if all(triplet[i] <= target[i] for i in range(3)):
                # A safe triplet can be merged freely. Record every position where it already equals the target value.
                for i in range(3):
                    if triplet[i] == target[i]:
                        found.add(i)
        # Merging all safe triplets gives target exactly when every position was reached by at least one of them.
        return len(found) == 3

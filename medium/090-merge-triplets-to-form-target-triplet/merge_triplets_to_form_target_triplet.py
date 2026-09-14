class Solution:
    def merge_triplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        found = set()
        for triplet in triplets:
            if all(triplet[i] <= target[i] for i in range(3)):
                for i in range(3):
                    if triplet[i] == target[i]:
                        found.add(i)
        return len(found) == 3

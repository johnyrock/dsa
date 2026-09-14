class Solution:
    # Return every distinct multiset of candidates (each index used at most once) that sums to target.
    def combination_sum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # Sorting puts equal values next to each other (so duplicates can be skipped) and in ascending order (so a too-big value ends the loop).
        candidates.sort()
        # The combinations found so far.
        result = []
        # The combination currently being built, one chosen candidate per recursion level.
        path = []

        # start: the first index we may still choose from; remaining: how much of target is left to fill.
        def backtrack(start: int, remaining: int) -> None:
            # remaining hit exactly zero, so path is a complete combination. Copy it, because path keeps mutating.
            if remaining == 0:
                result.append(path[:])
                return
            # Try each candidate at or after start; never look back, so each index is used at most once and every combination is built in sorted order.
            for i in range(start, len(candidates)):
                # Values are ascending, so once one is too big every later one is too, and the loop can stop rather than continue.
                if candidates[i] > remaining:
                    break
                # The same value at the same tree level would rebuild the same combination. Only the first copy at this level may start a branch; a copy right after the chosen one (i == start) is still allowed, so [1, 1, 6] survives.
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Choose candidates[i].
                path.append(candidates[i])
                # Recurse from i + 1 (not i) so this index cannot be reused, with the smaller remaining sum.
                backtrack(i + 1, remaining - candidates[i])
                # Undo the choice so the next iteration starts from the same prefix.
                path.pop()

        # Start with nothing chosen and the full target to fill.
        backtrack(0, target)
        return result

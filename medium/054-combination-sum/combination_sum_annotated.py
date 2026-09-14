class Solution:
    # Return every multiset of candidates (each reusable any number of times) that sums to target.
    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        # Sort so that once a candidate is too big for what remains, every later candidate is too. That makes `break` safe below.
        candidates = sorted(candidates)
        # The combinations found so far.
        result = []
        # The one combination under construction, shared by every recursive call and edited in place.
        path = []

        # Extend path with candidates at index >= start, needing exactly `remaining` more to hit the target.
        def backtrack(start: int, remaining: int) -> None:
            # Nothing left to pay: path is a complete combination. Copy it, because path keeps changing afterwards.
            if remaining == 0:
                result.append(path[:])
                return
            # Try each candidate from `start` onward. Never looking back before `start` is what stops [2,3] and [3,2] both appearing.
            for i in range(start, len(candidates)):
                # Sorted order means this candidate and everything after it overshoots; stop the loop instead of recursing into dead ends.
                if candidates[i] > remaining:
                    break
                # Choose: spend candidates[i].
                path.append(candidates[i])
                # Recurse with `i`, not `i + 1`: the same candidate may be reused, so it stays available.
                backtrack(i, remaining - candidates[i])
                # Undo: take it back so the next iteration starts from the same prefix.
                path.pop()

        # Start with nothing chosen and the whole target still owed.
        backtrack(0, target)
        return result

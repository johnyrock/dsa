class Solution:
    def is_valid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}  # closer -> opener
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack

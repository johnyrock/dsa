class Solution:
    # Define the function that takes the bracket string and returns True when it is balanced.
    def is_valid(self, s: str) -> bool:
        # Map each closing bracket to the opening bracket it must be matched with. Looking a character up here also tells us whether it is a closer at all.
        pairs = {")": "(", "]": "[", "}": "{"}  # closer -> opener
        # Create an empty list used as a stack of opening brackets that are still waiting to be closed. The last item is the most recent opener.
        stack = []
        # Walk through the string one character at a time, left to right.
        for ch in s:
            # A character that is a key of pairs is a closing bracket, so it has to close something.
            if ch in pairs:
                # Fail if there is nothing open to close, or if the most recent opener is the wrong kind. pop() removes that opener, since it is now settled.
                if not stack or stack.pop() != pairs[ch]:
                    # Either an unmatched closer or a crossed pair like "([)]", so the string is not valid.
                    return False
            # Otherwise the character is an opening bracket.
            else:
                # Push it on top of the stack so it becomes the next one that must be closed.
                stack.append(ch)
        # Every closer matched, so the string is valid only if no opener is left waiting, which is what an empty stack means.
        return not stack

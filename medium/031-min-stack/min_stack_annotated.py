class MinStack:
    def __init__(self):
        # The ordinary stack of every value pushed, in push order.
        self.stack = []
        # A second stack holding only the values that were the minimum at the moment they were pushed.
        # Its top is always the minimum of everything currently in self.stack.
        self.min_stack = []

    def push(self, val: int) -> None:
        # Every value goes onto the main stack unconditionally.
        self.stack.append(val)
        # It also goes onto min_stack if it is a new minimum. The <= (not <) matters: a duplicate of the current minimum
        # must be recorded too, otherwise popping one copy would wrongly discard the minimum for the other copy.
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Remove from the main stack. If the removed value is the current minimum, it was the one that put that entry
        # onto min_stack (min_stack only holds minimums-at-push-time), so that entry goes too and the previous minimum resurfaces.
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Plain stack top; nothing about minimums is involved.
        return self.stack[-1]

    def get_min(self) -> int:
        # The invariant makes this a single read instead of a scan.
        return self.min_stack[-1]

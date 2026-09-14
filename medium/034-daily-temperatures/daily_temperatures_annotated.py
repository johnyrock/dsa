class Solution:
    # For each day, return how many days until a strictly warmer temperature; 0 if none comes.
    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        # Default every day to 0. Days that never see a warmer day keep this value untouched.
        answer = [0] * len(temperatures)
        # Indices (not temperatures) of days still waiting for their warmer day.
        # From bottom to top the temperatures are decreasing, so the top is the coolest waiting day.
        stack = []
        for i, temp in enumerate(temperatures):
            # Today resolves every waiting day that is cooler than today. Because the stack is
            # decreasing, those are exactly the top entries; stop at the first one that is not cooler.
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                # The distance is measured in indices, which is why the stack holds indices.
                answer[j] = i - j
            # Today now waits for its own warmer day. Pushing after popping keeps the stack decreasing.
            stack.append(i)
        # Anything still on the stack never found a warmer day and keeps its 0.
        return answer

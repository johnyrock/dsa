# 088. Gas Station

**Difficulty:** Medium | **Pattern:** [greedy](../../patterns/greedy.md) ([explained](../../concepts/greedy.html)) | **Source:** LeetCode #134

## Problem

There are `n` gas stations on a circular route. Station `i` has `gas[i]` litres of fuel, and driving from station `i` to station `i + 1` costs `cost[i]` litres. You start with an empty tank at one station and must travel the whole circle once, clockwise.

Return the index of the starting station that lets you complete the circuit, or `-1` if no station does. The tests guarantee the answer is unique when it exists.

## Examples

```
Input:  gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3             # start at 3 with 4 litres: 4-1=3, +5-2=6, +1-3=4, +2-4=2, +3-5=0, back at 3

Input:  gas = [2,3,4], cost = [3,4,3]
Output: -1            # total gas 9 is less than total cost 10, no start can work

Input:  gas = [5,1,2,3,4], cost = [4,4,1,5,1]
Output: 4             # starting at 0 dies at station 3, and so would 1, 2, 3; only 4 survives
```

## Constraints

- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`
- the input is generated such that the answer is unique

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from simulating every start to a single pass that resets the candidate whenever the tank runs dry, with complexity.

## Follow-up

- Without the uniqueness guarantee, several starts may work. Return the smallest one; does the single pass still find it?
- What if you may drive counter-clockwise instead? Can you answer both directions in O(n)?
- Suppose the tank has a maximum capacity `cap`. Does the greedy argument still hold, and what breaks if not?

# 072. House Robber

**Difficulty:** Medium | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) ([explained](../../concepts/dynamic-programming.html)) | **Source:** LeetCode #198

## Problem

You are given `nums`, where `nums[i]` is the amount of money in house `i` along a street. You may rob any houses you like, except that robbing two adjacent houses trips the alarm.

Return the maximum amount you can rob without ever taking two neighbouring houses.

## Examples

```
Input:  nums = [2,7,9,3,1]
Output: 12            # houses 0, 2, 4: 2 + 9 + 1 = 12 beats 7 + 3 = 10

Input:  nums = [1,2,3,1]
Output: 4             # houses 0 and 2: 1 + 3 = 4

Input:  nums = [2,1,1,2]
Output: 4             # houses 0 and 3; skipping two in a row is allowed
```

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from trying every subset to a loop with two rolling variables, with complexity.

## Follow-up

- House Robber II (LeetCode #213) puts the houses in a circle so house 0 and house n-1 are adjacent. How do you reduce it to two runs of this function?
- House Robber III (LeetCode #337) arranges the houses as a binary tree. What pair of values does each node need to return?
- What changes if you must also report *which* houses were robbed, not just the total?

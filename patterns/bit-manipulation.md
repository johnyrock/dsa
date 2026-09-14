# Bit Manipulation

## When to use

- A problem asks about binary digits, parity, set bits, or powers of two.
- Equal values should cancel in pairs, which is often an XOR signal.
- You can build a result from a number's shifted prefix and its final bit.

## Templates

**Cancel pairs with XOR:**

```python
answer = 0
for value in values:
    answer ^= value
return answer
```

**Clear one set bit at a time:**

```python
count = 0
while n:
    n &= n - 1
    count += 1
```

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [easy/024 Single Number](../easy/024-single-number/) | Easy | duplicated values cancel with XOR |
| [easy/025 Number of 1 Bits](../easy/025-number-of-1-bits/) | Easy | clear the lowest set bit each pass |
| [easy/026 Counting Bits](../easy/026-counting-bits/) | Easy | shifted prefix plus final bit recurrence |
| [easy/027 Reverse Bits](../easy/027-reverse-bits/) | Easy | shift input bits into a fixed-width result |
| [easy/028 Missing Number](../easy/028-missing-number/) | Easy | XOR range values against input values |
| [medium/101 Sum of Two Integers](../medium/101-sum-of-two-integers/) | Medium | Binary addition splits into two independent parts: `a ^ b` is the sum of each bit… |

## Common mistakes

- Using arithmetic addition where XOR cancellation is needed.
- Forgetting that a fixed-width integer includes leading zero bits.
- Shifting a value before extracting the bit needed for the current iteration.

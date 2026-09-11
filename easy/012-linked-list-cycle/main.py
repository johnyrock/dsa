from linked_list_cycle import ListNode, Solution

solution = Solution()

a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)
a.next, b.next, c.next, d.next = b, c, d, b  # cycle back into b

print(solution.has_cycle(a))
print(solution.has_cycle(ListNode(1)))

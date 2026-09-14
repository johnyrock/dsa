from __future__ import annotations


class Node:
    def __init__(self, x: int, next: Node | None = None, random: Node | None = None) -> None:
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copy_random_list(self, head: Node | None) -> Node | None:
        old_to_new = {None: None}
        node = head
        while node is not None:
            old_to_new[node] = Node(node.val)
            node = node.next
        node = head
        while node is not None:
            copy = old_to_new[node]
            copy.next = old_to_new[node.next]
            copy.random = old_to_new[node.random]
            node = node.next
        return old_to_new[head]

from __future__ import annotations


class Node:
    def __init__(self, x: int, next: Node | None = None, random: Node | None = None) -> None:
        self.val = x
        self.next = next
        self.random = random


class Solution:
    # Deep-copy a list whose nodes have both next and random pointers, using a map from each original node to its copy.
    def copy_random_list(self, head: Node | None) -> Node | None:
        # Seed the map with None -> None so that looking up a null next or random pointer just yields None instead of a KeyError.
        old_to_new = {None: None}
        # Pass 1: create a fresh node for every original, keyed by the original node object (identity, not value: two nodes with equal val are different keys).
        node = head
        while node is not None:
            old_to_new[node] = Node(node.val)
            node = node.next
        # Pass 2: now that every copy exists, wire each copy's pointers by translating the original's targets through the map.
        node = head
        while node is not None:
            copy = old_to_new[node]
            # Translate next: the copy of node.next, which already exists from pass 1 (or None at the tail).
            copy.next = old_to_new[node.next]
            # Translate random the same way. It may point forward, backward, to itself, or to None; the map handles all four identically.
            copy.random = old_to_new[node.random]
            node = node.next
        # The copy of head is the head of the copied list. For an empty list this is old_to_new[None] == None.
        return old_to_new[head]

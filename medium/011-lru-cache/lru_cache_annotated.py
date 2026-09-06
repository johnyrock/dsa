# A doubly linked node. It stores its own key so that when it is evicted from the tail we can also delete it from the dictionary.
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        # The dictionary gives O(1) lookup by key. Its values are nodes, not plain values, so a hit also tells us WHERE the key sits in the recency order.
        self.nodes = {}        # key -> Node
        # Two sentinel nodes bracket the list. They are never removed, so "the node after head" and "the node before tail" always exist and no insert or unlink needs a None check.
        self.head = Node()     # sentinel: most recently used side
        self.tail = Node()     # sentinel: least recently used side
        self.head.next = self.tail
        self.tail.prev = self.head

    # Detach a node from wherever it is. O(1) because the node knows both its neighbours.
    def _unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Insert a node right after head, making it the most recently used.
    def _push_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        # A read is a use: move the node to the front so it is now the last candidate for eviction.
        self._unlink(node)
        self._push_front(node)
        return node.val

    def put(self, key, value):
        if key in self.nodes:
            # Update in place, then treat it as a use. The size does not change, so no eviction check is needed.
            node = self.nodes[key]
            node.val = value
            self._unlink(node)
            self._push_front(node)
            return
        # New key. If the cache is full, the least recently used node is the one just before tail; drop it from both structures.
        if len(self.nodes) == self.capacity:
            lru = self.tail.prev
            self._unlink(lru)
            del self.nodes[lru.key]
        # Create the node, index it, and make it the most recently used.
        node = Node(key, value)
        self.nodes[key] = node
        self._push_front(node)

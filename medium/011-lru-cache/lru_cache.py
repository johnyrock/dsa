class Node:
    def __init__(self, key: int = 0, val: int = 0) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.nodes = {}        # key -> Node
        self.head = Node()     # sentinel: most recently used side
        self.tail = Node()     # sentinel: least recently used side
        self.head.next = self.tail
        self.tail.prev = self.head

    def _unlink(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _push_front(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._unlink(node)
        self._push_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self._unlink(node)
            self._push_front(node)
            return
        if len(self.nodes) == self.capacity:
            lru = self.tail.prev
            self._unlink(lru)
            del self.nodes[lru.key]
        node = Node(key, value)
        self.nodes[key] = node
        self._push_front(node)

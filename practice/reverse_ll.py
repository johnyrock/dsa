class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def from_array(arr):
    list_node = ListNode()
    # print(f'list_node: {list_node}')
    curr = list_node
    print(f'curr: {curr.val}')

    for value in arr:
        # print(f'-----')
        curr.next = ListNode(value)
        # print(f'curr.next: {curr.val}')
        curr = curr.next
        # print(f'curr: {curr.val}')

    return list_node.next


def print_list(head):
    curr = head

    while curr:
        print(curr.val)
        curr = curr.next

head = from_array([1, 2, 3, 4, 5])

print_list(head)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

def to_linked_list(arr):
    head=ListNode()
    node=head

    for v in arr:
        node.next=ListNode(v)
        node=node.next
    return head.next

def to_array(linked_list):
    arr = []
    while linked_list is not None:
        arr.append(linked_list.val)
        linked_list = linked_list.next
    return arr


def reverse_ll(head):
    prev = None
    curr = head
    while curr:
        next_val_holder = curr.next
        curr.next = prev
        prev = curr
        curr = next_val_holder
    return prev


cases = [
    #value, expected
    ([1,2,3,4,5], [5,4,3,2,1])
]
def test_cases(cases):
    for val, exp in cases:
        res = to_array(reverse_ll(to_linked_list(val)))
        assert res == exp, f'input: {val}, output: {res}, FAIL'
        print(f'input: {val}, output: {res}, PASS')

test_cases(cases)
from kth_largest_element_in_a_stream import KthLargest

stream = KthLargest(3, [4, 5, 8, 2])
for value in [3, 5, 10, 9, 4]:
    print(stream.add(value))

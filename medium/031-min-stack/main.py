from min_stack import MinStack

stack = MinStack()

stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.get_min())   # -3
stack.pop()
print(stack.top())       # 0
print(stack.get_min())   # -2

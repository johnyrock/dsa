class Solution:
    # Evaluate a postfix (reverse Polish) expression given as a list of tokens and return its integer value.
    def eval_rpn(self, tokens: list[str]) -> int:
        # Operands wait here until an operator arrives to consume them.
        stack = []
        for token in tokens:
            # For every operator the two most recent operands are the arguments. The top of the stack is the RIGHT
            # operand (it was pushed last), the one below it is the LEFT operand. The order only matters for - and /.
            if token == "+":
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            elif token == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == "*":
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            elif token == "/":
                b, a = stack.pop(), stack.pop()
                # The problem truncates toward zero. Python's // floors toward negative infinity (6 // -132 == -1),
                # so divide as floats and truncate with int(), which gives 0 for 6 / -132.
                stack.append(int(a / b))
            else:
                # Anything that is not an operator is a number, possibly negative ("-11"), so int() is the parser.
                stack.append(int(token))
        # A valid expression leaves exactly one value on the stack: the result.
        return stack[-1]

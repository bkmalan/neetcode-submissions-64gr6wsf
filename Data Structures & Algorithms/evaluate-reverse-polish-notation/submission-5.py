class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                last = stack.pop()
                stack.append(stack.pop() - last)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                last = stack.pop()
                stack.append(int(stack.pop() / last))
            else:
                stack.append(int(token))
            print(stack)
        return stack.pop()
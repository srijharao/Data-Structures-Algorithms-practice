class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = '+'
        curr = 0

        for c in s + '+':
            if c == ' ':
                continue
            if c.isdigit():
                curr = curr * 10 + int(c)
            else:
                if op == '+':
                    stack.append(curr)
                elif op == '-':
                    stack.append(-curr)
                elif op == '/':
                    stack.append(int(stack.pop()/curr))
                elif op == '*':
                    stack.append(stack.pop() * curr)
                op = c
                curr = 0
            
        return sum(stack)

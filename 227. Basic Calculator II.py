class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        curr = 0
        prev_op = '+'

        for c in s + '+':
            if c == " ":
                continue
            if c.isdigit():
                curr = curr * 10 + int(c)
            else:
                if prev_op == '+':
                    stack.append(curr)
                elif prev_op == '-':
                    stack.append(-1 * curr)
                elif prev_op == '/':
                    stack.append(int(stack.pop()/curr))
                elif prev_op == '*':
                    stack.append(stack.pop()*curr)
                prev_op = c
                curr = 0
        
        return sum(stack)

        

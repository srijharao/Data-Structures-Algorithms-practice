#O(1) space
class Solution:
    def calculate(self, s: str) -> int:

        # stack = []
        result = 0
        lastnum = 0
        curr = 0
        prev_op = '+'

        for c in s + '+':
            if c == " ":
                continue
            if c.isdigit():
                curr = curr * 10 + int(c)
            else:
                if prev_op == '+':
                    result += lastnum
                    lastnum = curr
                    # stack.append(curr)
                elif prev_op == '-':
                    result += lastnum
                    lastnum = -1 * curr
                    # stack.append(-1 * curr)
                elif prev_op == '/':
                    lastnum = int(lastnum/curr)
                    # stack.append(int(stack.pop()/curr))
                elif prev_op == '*':
                    lastnum *= curr

                    # stack.append(stack.pop()*curr)
                prev_op = c
                curr = 0
        
        return result + lastnum #sum(stack)

        

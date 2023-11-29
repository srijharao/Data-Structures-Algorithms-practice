class Solution:
    def climbStairs(self, n: int) -> int:

        if(n == 1):
            return 1

        mem = [0] * n;
        mem[0] = 1;
        mem[1] = 2;
        
        i = 2
        while i < n:
            mem[i] = mem[i-1] + mem[i-2]
            i = i+1
        return mem[n-1]

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            half = helper(x, n//2)
            if n%2 == 0:
                return half * half
            if n%2 != 0:
                return x * half * half

        if n < 0:
            n = -n
            x = 1/x
        return helper(x,n)
#logn
#logn
        

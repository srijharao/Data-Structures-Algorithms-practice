#Iterative pow(x,n)
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            n = -n
            x = 1/x

        if x == 0:
            return 0
        if n == 0:
            return 1
        
        result = 1 
        while n > 0:
            if n%2 != 0: #odd
                result =  x * result
            x = x * x
            n = n//2
        return result
# time: O(logn)
# space: O(1) -- no recurssion stack
        

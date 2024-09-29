class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        steparr = [0]*n
        steparr[0] = 1
        steparr[1] = 2
        for i in range(2,n):
            steparr[i] = steparr[i-1] + steparr[i-2]
        return steparr[n-1]



        

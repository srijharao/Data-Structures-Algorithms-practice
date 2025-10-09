class Solution:
    def longestPalindrome(self, s: str) -> str:

        def ispalindrome(l,r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        ans = ""
        for i in range(len(s)):
            odd = ispalindrome(i,i)
            even = ispalindrome(i,i+1)
            if len(ans) < len(odd):
                ans = odd
            if len(ans) < len(even):
                ans = even

        return ans


        

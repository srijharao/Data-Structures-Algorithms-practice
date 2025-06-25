class Solution:
    def validPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s)-1

        def isPalindrome(string):
            return string == string[::-1] #O(n)


        while i < j: #O(n)
            if s[i] != s[j]:
                A = isPalindrome(s[i+1:j+1])
                B = isPalindrome(s[i:j])
                return A or B
            
            i += 1
            j -= 1
        return True
        

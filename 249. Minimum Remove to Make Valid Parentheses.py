class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        s = list(s)
        for i in range(0,len(s)):
            if s[i] == "(":
                stk.append((s[i],i))
            elif s[i] == ")":
                if not stk or stk.pop()[0] != "(":
                    s[i] = ""
        
        while stk:
            s[stk.pop()[1]] = ""
        
        return str("".join(s))

#time: O(n)
#space: O(n)


        

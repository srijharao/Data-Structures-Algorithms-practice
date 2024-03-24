class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1sorted = sorted(s1)
        s2sorted = sorted(s2)
        notEqualFlag = 0
        if (s1 == s2):
            return True
        if(s1sorted == s2sorted):
            for i in range(len(s1)):
                if(s1[i] != s2[i]):
                    notEqualFlag += 1
            if notEqualFlag == 2:
                return True
        return False
        

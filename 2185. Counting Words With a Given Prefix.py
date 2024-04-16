class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pl = len(pref)
        count = 0
        for s in words:
            if s[:pl] == pref:
                count +=1
        return count

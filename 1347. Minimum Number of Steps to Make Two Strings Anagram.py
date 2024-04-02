class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ctrS = Counter(s)
        ctrT = Counter(t)
        delta = 0
        for i in ctrS:
            if i not in ctrT:
                delta += ctrS[i]
            else:
                delta += max(ctrS[i]-ctrT[i], 0)
        return delta

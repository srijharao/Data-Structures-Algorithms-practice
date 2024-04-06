class Solution:
    def nextGreaterElement(self, n: int) -> int:
        m = list(str(n))

        j = len(m) -1

        while j > 0 and m[j-1] >= m[j]:
            j -= 1
        
        if j==0:
            return -1

        high = len(m)-1
        while high > j - 1 and m[high] <= m[j-1]:
            high -=1

        m[high], m[j-1] = m[j-1], m[high]
        m[j:] = m[j:][::-1]

        s = int("".join(m))
        return s if s <= 2**31 -1 else -1

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = res = max(piles)

        while i < j:
            mid = (i+j)//2
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas/mid)
            if hours <= h:
                j = mid
                res = min(res, mid)
            else:
                i = mid + 1
        return res

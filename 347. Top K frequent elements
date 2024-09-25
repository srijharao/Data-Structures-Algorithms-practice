class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        heap = []
        res = []
        for i in nums:
            mp[i] = 1+ mp.get(i,0)
        
        for key, val in mp.items():
            heapq.heappush(heap, (-val, key))
        
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapnums = [-num for num in nums]

        heapq.heapify(heapnums) #O(n)

        i = 1
        while i <= k:
            ans = heapq.heappop(heapnums) #O(logn)
            i += 1
        
        return -1 * ans

        #Time: O(n + klogn)
        #Space: O(n)
        

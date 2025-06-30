class SparseVector:
    def __init__(self, nums: List[int]):
        #time: O(n) Space: O(K)
      
        self.pairs = []
        for idx, val in enumerate(nums):
            if val != 0:
                self.pairs.append([idx,val])
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        #time: O(klogn) Space: O(1) k times on shorter list. logn times on longer list

        shorter, longer = (self.pairs, vec.pairs) if len(self.pairs) < len(vec.pairs) else (vec.pairs, self.pairs)

        p = 0
        result = 0

        while p < len(shorter):
            i = 0
            j = len(longer) -1
            while i<=j:
                mid = (i+j) // 2
                if longer[mid][0] == shorter[p][0]:
                    result += longer[mid][1] * shorter[p][1]
                    break
                elif longer[mid][0] < shorter[p][0]:
                    i = mid + 1
                else:
                    j = mid - 1
            p += 1
        return result
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

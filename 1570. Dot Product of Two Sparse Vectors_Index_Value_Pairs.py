
class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for i in range(len(nums)):
            if nums[i] != 0:
                self.pairs.append([i, nums[i]])
        #time : O(n) 
        #space: O(k) non zero values
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        p = q = 0
        result = 0

        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                result += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1
        
        return result
      
        #time : O(m+n) 
        #space: O(1)

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

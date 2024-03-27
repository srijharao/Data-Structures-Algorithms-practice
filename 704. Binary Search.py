class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0 if target == nums[0] else -1
        
        i = 0
        j = len(nums) - 1

        while i <= j: 
            median = (i + j)//2
            if target == nums[median]:
                return median
            if target < nums[median]:
                j = median - 1
            if target > nums[median]:
                i = median + 1
        
        return -1

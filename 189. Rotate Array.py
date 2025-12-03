class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #O(n), O(1)
        K = k%len(nums)

        #reverse entire array
        l = 0
        r = len(nums)-1
        while l<r:
            nums[l],nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        #reverse first k elements
        l = 0
        r = K-1
        while l < r:
            nums[l],nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        #reverse remaining elements
        l = K
        r = len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        



        

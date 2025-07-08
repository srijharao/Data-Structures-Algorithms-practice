class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = None
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                idx = i-1
                break
        if idx is None:
            nums.reverse()
            return
        
        for i in range(len(nums)-1,idx,-1):
            if nums[i]> nums[idx]:
                nums[idx], nums[i] = nums[i], nums[idx]
                nums[idx+1:] = nums[idx+1:][::-1]
                return
#O(N)
#O(1)

        

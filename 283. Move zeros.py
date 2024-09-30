class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        j = i+1
        while i< j and j< len(nums):
            temp = float('-inf')
            if nums[i] == 0:
                if nums[j] != 0:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    i += 1
                    j+=1
                else:
                    j+=1
            else:
                i+=1
                j+=1
        return nums

        

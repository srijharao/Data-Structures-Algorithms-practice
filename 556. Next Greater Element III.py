class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        i = len(nums)-1
        high = len(nums)-1

        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i ==0:
            return -1

        while high > i-1 and nums[high] <= nums[i-1]:
            high -= 1
        
        nums[high] , nums[i-1] = nums[i-1] , nums[high]
        nums[i:] = nums[i:][::-1]

        retVal = int("".join(nums))
        return retVal if retVal <= 2**31-1 else -1

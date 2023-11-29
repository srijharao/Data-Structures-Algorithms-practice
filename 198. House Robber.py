class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        nums[1] = max(nums[0], nums[1]);

        i = 2;
        while i < len(nums) :
            nums[i] = max(nums[i-1], nums[i]+nums[i-2])

            i = i+1;
        return nums[len(nums) -1]

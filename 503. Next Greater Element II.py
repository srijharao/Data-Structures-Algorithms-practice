class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        nextHigh = {}
        # nums2 = nums + nums
        for i in list(range(len(nums))) * 2:
            while stack and nums[stack[-1]] < nums[i]:
                nextHigh[stack.pop()] = nums[i]
            stack.append(i)
        
        return [nextHigh.get(i,-1) for i in range(len(nums))]

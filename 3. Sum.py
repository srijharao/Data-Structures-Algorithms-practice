class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        resSet = set()
        
        for i in range(len(nums)):
            j = i + 1
            k = len(nums)-1
            while(j < k):
                if (nums[i] + nums[j] + nums[k] == 0):
                    resSet.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif (nums[i] + nums[j] + nums[k] > 0):
                    k -= 1
                else:
                    j += 1

        return [list(i) for i in resSet]

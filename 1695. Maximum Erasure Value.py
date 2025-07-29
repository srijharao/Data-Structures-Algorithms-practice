class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        maxscore = 0
        currscore = 0
        left = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                currscore = currscore - nums[left]
                left += 1

            seen.add(nums[right])
            currscore += nums[right]
            maxscore = max(maxscore, currscore)

        return maxscore
#O(n)
        

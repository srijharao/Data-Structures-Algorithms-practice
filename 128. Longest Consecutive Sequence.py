class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        curr_len = 0

        for n in nums:
            if n-1 not in nums:
                curr_len = 1
                next_num = n+1
                while next_num in nums:
                    curr_len += 1
                    next_num += 1
            max_len = max(max_len, curr_len)
        
        return max_len


#O(n) O(n)

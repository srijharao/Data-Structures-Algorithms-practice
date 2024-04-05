class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextHigh = {}
        stack = []

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1] :
                nextHigh[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        return [nextHigh.get(i,-1) for i in nums1]

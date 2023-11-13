class Solution:
    def maxArea(self, height: List[int]) -> int:
        a = 0
        b = len(height) -1
        most = -inf

        while a < b:
            if height[a] < height[b]:
                most = max(most, abs(a-b) * height[a])
                a = a + 1
            else:
                most = max(most, abs(a-b) * height[b])
                b = b - 1
        return most

        

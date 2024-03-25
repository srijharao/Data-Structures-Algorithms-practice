class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        if max(worker) < min(difficulty):
            return 0
        maxProfit = curProfit = idx = 0

        difficulty, profit = zip(*sorted(zip(difficulty, profit)))

        for i in sorted(worker):
            while idx < len(difficulty) and i >= difficulty[idx]:
                curProfit = max(curProfit,profit[idx])
                idx += 1
            maxProfit += curProfit
        return maxProfit

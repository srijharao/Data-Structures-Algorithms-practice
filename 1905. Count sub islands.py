class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def dfs(i,j):
            if i < 0 or j<0 or i>=len(grid1) or j>=len(grid1[0]) or grid2[i][j] == 0:
                return
            grid2[i][j] = 0
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                # 
                if grid1[i][j] != grid2[i][j]:
                    dfs(i,j)
        count = 0           
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    count += 1
                    dfs(i,j)
        return count

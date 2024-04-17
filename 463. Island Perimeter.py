class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #All water border is perimeter

        rows = len(grid)
        cols = len(grid[0])

        def isWater(i,j):
            if i < 0 or i>= rows or j >= cols or j< 0:
                return 1
            if grid[i][j] == 0:
                return 1
            return 0

        def getWaterSides(i,j):
            water = isWater(i+1, j) + isWater(i-1, j) + isWater(i, j+1) + isWater(i, j-1)
            return water

        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += getWaterSides(i,j)
        return perimeter
                    
        

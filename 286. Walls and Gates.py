class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        cols = len(rooms[0])

        def dfs(i,j,dist):
            if i < 0 or j < 0 or i>= rows or j>=cols or rooms[i][j] <= dist+1 or rooms[i][j] <= 0:
                return
            
            rooms[i][j] = dist + 1

            dfs(i+1,j,dist +1)
            dfs(i-1,j,dist +1)
            dfs(i,j+1,dist +1)
            dfs(i,j-1,dist +1)

        dist = 0
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    dfs(i+1,j,dist)
                    dfs(i-1,j,dist)
                    dfs(i,j+1,dist)
                    dfs(i,j-1,dist)

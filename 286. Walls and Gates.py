class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # queue = deque()
        def inBounds(i,j,rows,cols):
            if i >= 0 and i < rows and j >= 0 and j < cols:
                return True
            return False

        def dfs(i,j,steps):
            if not inBounds(i,j,len(rooms),len(rooms[0])) or rooms[i][j] == -1:
                return
            
            if rooms[i][j] !=0 and rooms[i][j] > 1+steps:
                # steps += 1
                rooms[i][j] = min(rooms[i][j], steps+1)
                dfs(i+1,j,steps+1)
                dfs(i-1,j,steps+1)
                dfs(i,j+1,steps+1)
                dfs(i,j-1,steps+1)
            
        steps = 0
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    dfs(i+1,j,steps)
                    dfs(i-1,j,steps)
                    dfs(i,j+1,steps)
                    dfs(i,j-1,steps)

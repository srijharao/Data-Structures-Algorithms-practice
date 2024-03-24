class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minLength = float('inf')
        minIdx = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                manhattan = abs(x - points[i][0]) + abs(y-points[i][1])
                if(manhattan < minLength):
                    minLength = manhattan
                    minIdx = i
        return minIdx

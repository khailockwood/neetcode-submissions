from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        visited = set()

        neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        minutes = 0
        numFresh = 0
        numRotten = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    numRotten += 1
                    queue.append((i, j))
                if grid[i][j] == 1:
                    numFresh += 1
                   
        while queue and numFresh > 0:
            for i in range(len(queue)):
                currR, currC = queue.popleft()
                
                for r, c in neighbors:
                    if (currR + r < 0 or currC + c < 0) or (currR + r == rows or currC + c == cols) or grid[currR + r][currC + c] == 0 or (currR + r,currC + c) in visited:
                        continue
                    if (grid[currR + r][currC + c] == 1):
                        grid[currR + r][currC + c] = 2
                        numFresh -= 1
                        numRotten += 1
                        queue.append((currR + r, currC + c))
                        visited.add((currR + r, currC + c))
            minutes += 1
        return minutes if numFresh == 0 else -1
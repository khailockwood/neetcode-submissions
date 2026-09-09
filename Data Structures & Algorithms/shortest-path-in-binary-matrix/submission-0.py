from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])


        if grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0:
            return -1

        queue = deque()
        visited = set()
        length = 1
        queue.append((0, 0))
        visited.add((0, 0))

        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, -1], [1, 1], [-1, -1], [-1, 1]]
        while queue:
            for i in range(len(queue)):
                currR, currC = queue.popleft()

                if currR == rows - 1 and currC == cols - 1:
                    return length

                for r, c in neighbors:
                   if (currR + r < 0 or currC + c < 0) or (currR + r == rows or currC + c == cols) or grid[currR + r][currC + c] == 1 or (currR + r,currC + c) in visited:
                        continue
                   queue.append((currR + r, currC + c))
                   visited.add((currR + r, currC + c))
            length += 1
        return -1
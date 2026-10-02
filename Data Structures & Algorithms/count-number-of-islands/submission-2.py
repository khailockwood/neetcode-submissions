class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islandCount = 0

        def dfs(r, c, visited):
            if (not (0 <= r < rows) or not (0 <= c < cols) or grid[r][c] != "1" or (r,c) in visited):
                return 0

            else:
                visited.add((r,c))
                grid[r][c] = "0"
                return dfs(r + 1, c, visited) or dfs(r, c + 1, visited) or dfs(r - 1, c, visited) or dfs(r, c - 1, visited)

            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islandCount += 1
                    dfs(i, j, visited)

        return islandCount
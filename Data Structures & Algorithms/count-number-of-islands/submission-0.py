class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0

        def dfs(row, column):
            if not (0 <= row < len(grid)) or not (0 <= column < len(grid[0])) or grid[row][column] != '1':
                return
            else:
                grid[row][column] = '0'
                dfs(row + 1, column)
                dfs(row - 1, column)
                dfs(row, column + 1)
                dfs(row, column - 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islandCount += 1
        return islandCount
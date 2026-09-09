class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0

        def dfs(row, column, area):
            if not (0 <= row < len(grid)) or not (0 <= column < len(grid[0])) or grid[row][column] != 1:
                return 0 #there's no land this way, don't add to area, go back up to previous call
            else:
                grid[row][column] = 0
                return 1 + dfs(row, column + 1, area) + dfs(row, column - 1, area) + dfs(row + 1, column, area) + dfs(row - 1, column, area) #the 1 + ... account for current cell (adding 1 to area), then every call s after search neighbors
            
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res = dfs(i, j, 0)
                    if (res > self.maxArea):
                        self.maxArea = res

        return self.maxArea
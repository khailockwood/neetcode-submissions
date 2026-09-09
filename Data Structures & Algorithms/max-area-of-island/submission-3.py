class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0

        def dfs(row, column, area):
            if not (0 <= row < len(grid)) or not (0 <= column < len(grid[0])) or grid[row][column] != 1:
                #area = 0
                return 0
            else:
                #if area >= self.maxArea:
                    #self.maxArea = area
                grid[row][column] = 0
                return 1 + dfs(row, column + 1, area) + dfs(row, column - 1, area) + dfs(row + 1, column, area) + dfs(row - 1, column, area)
            
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res = dfs(i, j, 0)
                    print(res)
                    if (res > self.maxArea):
                        self.maxArea = res
                    print("found a 1 at: " + str(i) + str(j))
                    print("max area: " + str(self.maxArea))

        return self.maxArea
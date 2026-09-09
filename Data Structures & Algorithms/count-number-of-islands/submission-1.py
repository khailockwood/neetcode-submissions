class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0

        def dfs(row, column):
            if not (0 <= row < len(grid)) or not (0 <= column < len(grid[0])) or grid[row][column] != '1':
                return
            else:
                grid[row][column] = '0' #searched, so turn to 0, no double searching
                dfs(row + 1, column) #search all the way this way until we either hit out of bounds or a 0
                dfs(row - 1, column) #then will go back to starting [row][column], search this way until we hit same above base case
                dfs(row, column + 1)
                dfs(row, column - 1)
                #by end we've search every direction, replaced the island we've searched with 0's, and then the next iteration of the for loop will go and will loop until we find another '1', and do this all again
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islandCount += 1
        return islandCount
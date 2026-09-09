class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startingColor = image[sr][sc]
        if startingColor == color:
            return image
        def dfs(row, column):
            r, c = len(image), len(image[0])
            if ((min(row, column) < 0) or not(0 <= row < r and column < c) or image[row][column] != startingColor) :
                return
            else:
                image[row][column] = color
                dfs(row + 1, column)
                dfs(row - 1, column)
                dfs(row, column + 1)
                dfs(row, column - 1)
        dfs(sr, sc)
        return image


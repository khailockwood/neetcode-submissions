class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = {}
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        def memo(r, c, cache):
            if r == rows or c == cols or obstacleGrid[r][c] == 1:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1

            if (r,c) in cache:
                return cache[(r, c)]

            cache[(r, c)] = memo(r, c + 1, cache) + memo(r + 1, c, cache)

            return cache[(r, c)]

        return memo(0, 0, cache)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        m = len(matrix)
        n = len(matrix[0])
        right = (m * n) - 1
        
        while left <= right:
            mid = (left + right) // 2

            current = matrix[mid // n][mid % n]
            print(current)
            if current == target:
                return True
            if current < target:
                left = mid + 1
            if current > target:
                right = mid - 1

        return False
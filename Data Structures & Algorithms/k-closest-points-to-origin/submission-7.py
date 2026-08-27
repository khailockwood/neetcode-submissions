import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min = 0
        mins = []
        distances = []
        for i in range(len(points)):
            distance = (points[i][0] ** 2) + (points[i][1] ** 2)
            addTuple = (distance, points[i])
            distances.append(addTuple)

        length = len(distances) - 1
        mins = self.quickSelect(distances, 0, length, k)
        print(mins)
        return mins

    def quickSelect(self, arr: list[float], s: int, e: int, k: int) -> list[int]:
        if e - s + 1 <= 1:
            return [point[1] for point in arr[:k]]

        pivot = arr[e]
        left = s #pointer for left side

        for i in range(s, e):
            if arr[i] < pivot:
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left += 1
        
        #switch to right side
        arr[e] = arr[left]
        arr[left] = pivot
        if left == k:
            return [point[1] for point in arr[:k]]

        #recurse left side
        if left > k:
            return self.quickSelect(arr, s, left - 1, k)

        #recurse right side
        if left <= k:
            return self.quickSelect(arr, left + 1, e, k)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            print(mid)

            
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: # if left side sorted
                if nums[left] <= target < nums[mid]: # if target in between far left and mid
                    right = mid - 1
                else:
                    left = mid + 1

            elif nums[right] >= target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1

            
        
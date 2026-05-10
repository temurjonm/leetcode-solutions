class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(nums, target):
            left, right = 0, len(nums)-1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        for row in matrix:
            if binarySearch(row, target):
                return True
        return False
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in myMap:
                return [myMap[diff], index]

            myMap[num] = index
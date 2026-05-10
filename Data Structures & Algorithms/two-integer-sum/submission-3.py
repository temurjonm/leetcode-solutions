'''
     t = 7
    [3,4,5,6]
     0    

    7 - 3 = 4
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in mapping:
                return [mapping[comp], i]

            mapping[num] = i

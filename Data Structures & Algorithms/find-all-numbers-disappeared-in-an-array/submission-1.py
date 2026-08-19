class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        sorted_set = set(range(1, n + 1))

        for num in nums:
            sorted_set.discard(num)

        return list(sorted_set) 
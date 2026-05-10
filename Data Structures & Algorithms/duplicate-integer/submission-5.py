class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_duplicate = set()

        for num in nums:
            if num in has_duplicate:
                return True

            has_duplicate.add(num)

        return False
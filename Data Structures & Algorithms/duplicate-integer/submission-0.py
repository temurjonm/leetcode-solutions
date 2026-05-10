class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDuplicate = set()

        for num in nums:
            if num in hasDuplicate:
                return True
            hasDuplicate.add(num)

        return False

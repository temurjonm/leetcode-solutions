class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        current_sum = 0
        total = 0

        for num in nums:
            current_sum += num
            needed = current_sum - k
            total += prefix_sum.get(needed, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return total
        
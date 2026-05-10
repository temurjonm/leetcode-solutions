class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSubarray = 0
        maxSubarray = float('-inf')

        for num in nums:
            currSubarray = max(currSubarray + num, num)
            maxSubarray = max(maxSubarray, currSubarray)

        return maxSubarray
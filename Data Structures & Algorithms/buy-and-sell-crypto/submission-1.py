class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfits = 0

        left = 0

        for right, price in enumerate(prices):
            if prices[right] < prices[left]:
                left = right

            maxProfits = max(maxProfits, prices[right] - prices[left])
            
        return maxProfits
            
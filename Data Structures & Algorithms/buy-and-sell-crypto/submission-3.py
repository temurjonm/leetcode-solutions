class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''
        [10,1,5,6,7,1]
            s
              b

            if b < s:
                s = b

            
        '''
        buy = 0
        max_profit = 0

        for sell in range(len(prices)):
            if prices[sell] < prices[buy]:
               buy = sell
            else:
                max_profit = max(max_profit, prices[sell] - prices[buy])
        
        return max_profit




            

    
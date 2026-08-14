class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    /**
     *       s
     * [10,1,5,6,7,1]
     *     b
     * s-b
     * 
     */
    maxProfit(prices: number[]): number {
        let max_profit = 0
        let buy = 0

        for (let sell = 0; sell < prices.length; sell++) {
            if (prices[sell] < prices[buy]) {
                buy = sell
            } 
            else {
                max_profit = Math.max(max_profit, prices[sell] - prices[buy])
            }
        }

        return max_profit

    }
}

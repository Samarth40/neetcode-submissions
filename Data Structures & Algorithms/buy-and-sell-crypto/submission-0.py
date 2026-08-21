class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] > prices[i]:
                    curr_profit = prices[j] - prices[i]
                    profit = max(curr_profit,profit)
        return profit

                
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = left + 1
        while right < len(prices):
            if left == len(prices) - 1 :
                break
            if prices[left] > prices[right]:
                left = right
            else:
                curr = prices[right] - prices[left]
                profit = max(curr,profit)
            right += 1
    
        return profit

                
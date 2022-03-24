class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                profit = max(profit, prices[i]-min_price)
        return profit
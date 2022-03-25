class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float('inf')
        
        for i in range(len(prices)):
            # If prices are going down (decreasing), just update min_price
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                # if the prices are more than the min_price
                # calculate the difference (and add to profit)
                profit += prices[i] - min_price
                min_price = prices[i]
                
        return profit
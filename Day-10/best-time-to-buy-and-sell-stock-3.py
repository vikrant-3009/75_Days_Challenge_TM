class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = [0] * n
        right = [0] * n
        left_min, right_max = prices[0], prices[-1]
        
        for i in range(1, n):
            left[i] = max(left[i-1], prices[i]-left_min)
            if prices[i] < left_min:
                left_min = prices[i]
        
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], right_max-prices[i])
            if prices[i] > right_max:
                right_max = prices[i]
        
        profit = -1
        for i in range(1, n):
            profit = max(profit, left[i-1] + right[i])
        profit = max(profit, left[-1], right[-1])
        
        # print(left, right)
        return profit
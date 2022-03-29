class Solution:
    # O(n) time and O(n) space
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        for i in range(len(time)):
            time[i] %= 60
        # print(time)
        
        d = {}
        for i in time:
            d[i] = d.get(i, 0) + 1
        
        pairs = 0
        for i in d:
            if i == 0 or i == 30:
                pairs += (d[i] * (d[i]-1)) // 2
                
            elif 60 - i in d:
                pairs += d[i] * d[60-i]
                d[i] = 0
                d[60-i] = 0
        
        return pairs
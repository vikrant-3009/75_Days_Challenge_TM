class Solution:    
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s, e = k-1, len(cardPoints)-1
        ans = sum(cardPoints[:k])
        sum1 = sum(cardPoints[:k])
        while s >= 0:
            sum1 -= cardPoints[s]
            s -= 1
            sum1 += cardPoints[e]
            e -= 1
            ans = max(ans, sum1)
        
        return ans
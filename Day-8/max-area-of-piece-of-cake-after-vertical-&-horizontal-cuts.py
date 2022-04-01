class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        h1, v1 = len(horizontalCuts), len(verticalCuts)
        mod = 10 ** 9 + 7
        horizontalCuts.sort()
        verticalCuts.sort()
        max_h, max_v = horizontalCuts[0], verticalCuts[0]
        
        for i in range(1, h1):
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i-1]) % mod
        max_h = max(max_h, h - horizontalCuts[h1-1]) % mod
        
        for i in range(1, v1):
            max_v = max(max_v, verticalCuts[i] - verticalCuts[i-1]) % mod
        max_v = max(max_v, w - verticalCuts[v1-1]) % mod
        
        return (max_h * max_v) % mod
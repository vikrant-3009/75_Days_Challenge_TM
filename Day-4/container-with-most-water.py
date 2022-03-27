class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        max_area = -1
        
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)
            if height[l] == height[r]:
                if height[l+1] > height[r-1]:
                    l += 1
                else:
                    r -= 1
                    
            elif height[l] < height[r]:
                l += 1
                
            else:
                r -= 1
                
        return max_area
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if n < 3 or nums[0] > 1:
            return []
        
        ans = set()
        i = 0
        while i < n-2:
            j, k = i+1, n-1
            
            while j < k:
                x = (nums[j] + nums[k])
                
                if x == abs(nums[i]):
                    ans.add((nums[i], nums[j], nums[k]))
                    j, k = j+1, k-1
                    
                elif x > abs(nums[i]):
                    k -= 1
                    
                else:
                    j += 1
            i += 1
            
        return ans
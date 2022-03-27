class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        x = nums[0]
        d[nums[0]] = 1
        s = 0
        if nums[0] == k:
            s += 1
            
        for i in range(1, len(nums)):
            x += nums[i]
            if x == k:
                s += 1
                
            if x-k in d:
                s += d[x-k]
                
            d[x] = d.get(x, 0) + 1
        
        return s
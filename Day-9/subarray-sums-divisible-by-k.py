class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] %= k
            
        s = 0
        ans = 0
        d = {}
        for i in range(n):
            s += nums[i]
            s %= k
            if s % k in d:
                ans += d[s]
                
            if s % k == 0:
                ans += 1
                
            d[s] = d.get(s, 0) + 1
            
        return ans
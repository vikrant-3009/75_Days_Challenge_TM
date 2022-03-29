class Solution:
    def incr_l(self, nums, l, r):
        l += 1
        while l < r and nums[l] == nums[l-1]:
            l += 1
        return l
    
    def incr_r(self, nums, l, r):
        r -= 1
        while l < r and nums[r] == nums[r+1]:
            r -= 1
        return r
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        i = 0
        n = len(nums)
        nums.sort()
        ans = []
        while i < n-3:
            j = i+1
            while j < n-2:
                x = nums[i] + nums[j]
                remain = target - x
                l, r = j+1, n-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == remain:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l = self.incr_l(nums, l, r)
                        r = self.incr_r(nums, l, r)
                    elif s < remain:
                        l = self.incr_l(nums, l, r)
                    else:
                        r = self.incr_r(nums, l, r)
                j += 1
                while j < n-2 and nums[j] == nums[j-1]:
                    j += 1
            i += 1
            while i < n-3 and nums[i] == nums[i-1]:
                i += 1
        
        return ans
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p, q = -1, -1
        for i in range(n):
            if nums[i] == 0:
                p = i
                break
        for i in range(n):
            if nums[i] != 0:
                q = i
                break
        
        if p == -1 or q == -1:
            return nums
        
        # p = zero 
        # q = non-zero
        
        i = q
        while i < n:
            if nums[i] != 0 and p < i:
                nums[i], nums[p] = nums[p], nums[i]
                while p < n and nums[p] != 0:
                    p += 1
            i += 1
        
        return nums
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        max_num = nums[i]
        while i >= 0:
            if nums[i] < max_num:
                break
            else:
                max_num = nums[i]
            i -= 1
        
        if i < 0:
            nums.sort()
        else:
            for j in range(n-1, i, -1):
                if nums[i]-nums[j] < 0:
                    nums[i], nums[j] = nums[j], nums[i]        
                    break
            nums[i+1 : ] = sorted(nums[i+1 : ])
            
        return nums
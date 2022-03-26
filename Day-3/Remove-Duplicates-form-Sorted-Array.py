class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        n = len(nums)
        if n == 1:
            return 1
        
        curr = nums[i]
        while j < n:
            if curr == nums[j]:
                # move to 2nd duplicate element 
                # (if i == 0 or i is at 1st occurance of duplicate elements)
                if i == 0:
                    i += 1
                # if previous element is grater then stay there
                elif nums[i-1] != nums[i] and nums[i-1] < nums[i]:
                    i += 1
            elif i == 0 or nums[i-1] < nums[i]:
                curr = nums[j]
                i += 1
            else:
                nums[i] = nums[j]
                curr = nums[j]
                i += 1
            j += 1
        
        if i == n-1 and nums[i] != nums[i-1]:
            return n
            
        return i
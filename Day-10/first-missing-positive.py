class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1
        
        # Mark all the visited indexes (i.e. through the numbers in the array) as negative 
        for i in range(n):
            # print(i)
            if abs(nums[i]) <= n:
                # print(abs(nums[i])-1)
                if nums[abs(nums[i])-1] > 0:
                    nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
                    
        for i in range(n):
            if nums[i] >= 0:
                return i+1
        
        return n+1
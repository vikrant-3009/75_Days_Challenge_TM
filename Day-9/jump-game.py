class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        index_to_reach = n-1
        
        for i in range(n-2, -1, -1):
            if (i + nums[i]) >= index_to_reach:
                index_to_reach = i
        
        if index_to_reach == 0:
            return True
        
        return False
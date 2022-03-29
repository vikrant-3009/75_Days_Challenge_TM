class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        s = float('inf')
        closest = float('inf')
        while i < n-2:
            remain = target - nums[i]
            j, k = i+1, n-1
            while j < k:
                x = nums[j] + nums[k]
                y = 0
                # y will store the difference between the sums of nums at jth and kth index and the remain element 
                if x <= remain:
                    y = remain - x 
                else:
                    y = x - remain
                
                # closest will contain min possible closest difference
                if y < closest:
                    closest = y
                    s = nums[i] + x
                    
                if x == remain:
                    return s
                elif x < remain:
                    j += 1
                else:
                    k -= 1
            i += 1
        
        return s
                    
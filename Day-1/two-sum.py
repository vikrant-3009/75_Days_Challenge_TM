class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]
                
        res = []
        for i in nums:
            if (target - i) in d:
                # check if i == target-i and i occurs more than once
                if i == target-i and len(d[i]) == 1:
                    continue
                    
                res.append(d[i][0])
                if i == target-i:
                    res.append(d[i][1])
                else:
                    res.append(d[target-i][0])
                break
        
        return res
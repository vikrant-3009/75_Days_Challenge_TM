class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        s1 = set()
        pairs = 0
        if k == 0:
            s = set()
            for i in nums:
                if i not in s1:
                    s1.add(i)
                elif i not in s:
                    pairs += 1
                    s.add(i)
        else:
            s = set(nums)
            for i in nums:
                if i not in s1:
                    if i+k in s:
                        pairs += 1
                        s1.add(i)
                    
        return pairs
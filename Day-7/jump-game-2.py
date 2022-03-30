class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [10000] * n
        ans[0] = 0
        for i in range(n):
            for j in range(1, nums[i]+1):
                if i+j < n:
                    ans[i+j] = min(ans[j+i], ans[i] + 1)
                    if i+j == n-1:
                        return ans[i+j]
        return ans[n-1]
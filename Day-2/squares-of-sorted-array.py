class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        i, j = 0, len(nums)-1
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                ans.append(nums[i] ** 2)
                i += 1
            else:
                ans.append(nums[j] ** 2)
                j -= 1
        return ans[::-1]
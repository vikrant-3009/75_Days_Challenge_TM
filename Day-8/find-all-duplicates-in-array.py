class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        # Elements in the array are valid indexes
        for i in range(len(nums)):
            # go to the index => (value-1) and make the value at that index negative
            # this will show we have visited that index
            idx = abs(nums[i]) - 1
            # if we are visiting the index, where negative value is present
            # then the current value is duplicate (as it's index is already visited)
            if nums[idx] < 0:
                ans.append(abs(nums[i]))
            else:
                nums[idx] = -nums[idx]
        return ans
class Solution:
    # Boyer Moore Majority Voting Algorithm
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        curr_count = 1
        for i in range(1, len(nums)):
            if nums[i] == curr:
                curr_count += 1
            else:
                if curr_count == 0:
                    curr = nums[i]
                else:
                    curr_count -= 1
        return curr
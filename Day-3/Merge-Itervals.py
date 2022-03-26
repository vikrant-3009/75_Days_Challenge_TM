class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = intervals[0][0]
        j = intervals[0][1]
        ans = []
        
        for k in range(1, len(intervals)):
            if intervals[k][0] <= j:
                j = max(j, intervals[k][1])
            else:
                ans.append([i, j])
                i, j = intervals[k][0], intervals[k][1]
        ans.append([i, j])
        
        return ans
class Solution:
    def solve(self, candidates, target, partial_ans, n, i):
        if target == 0:
            self.ans.append(partial_ans[:])
            return 
        
        if target < 0 or i == n:
            return
        
        partial_ans.append(candidates[i])
        self.solve(candidates, target-candidates[i], partial_ans, n, i)
        partial_ans.pop()
        self.solve(candidates, target, partial_ans, n, i+1)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        n = len(candidates)
        self.solve(candidates, target, [], n, 0)
        
        return self.ans
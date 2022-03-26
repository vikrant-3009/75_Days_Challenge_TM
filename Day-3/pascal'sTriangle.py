class Solution:
    def solve(self, i, j, partial_ans, n):
        if i == 0 or j == 0:
            partial_ans.append(1)
            return 
        
        self.solve(i, j-1, partial_ans, n)
        if j < n:
            partial_ans.append(self.ans[i-1][j-1] + self.ans[i-1][j])
        else:
            partial_ans.append(self.ans[i-1][j-1])
        return
        
    def generate(self, numRows: int) -> List[List[int]]:
        self.ans = []
        for i in range(numRows):
            partial_ans = []
            self.solve(i, i, partial_ans, i)
            self.ans.append(partial_ans[:])
            
        return self.ans
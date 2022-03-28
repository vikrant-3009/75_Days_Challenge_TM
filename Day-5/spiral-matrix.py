class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, down, left, right = 0, m-1, 0, n-1
        dirn = 0
        ans = []
        while left <= right and top <= down:
            if dirn == 0: # left to right
                for i in range(left, right+1):
                    ans.append(matrix[top][i])
                top += 1
            
            elif dirn == 1: # top to down
                for i in range(top, down+1):
                    ans.append(matrix[i][right])
                right -= 1
                
            elif dirn == 2: # right to left
                for i in range(right, left-1, -1):
                    ans.append(matrix[down][i])
                down -= 1
                
            elif dirn == 3: # down to top
                for i in range(down, top-1, -1):
                    ans.append(matrix[i][left])
                left += 1
            
            dirn = (dirn + 1) % 4
            
        return ans
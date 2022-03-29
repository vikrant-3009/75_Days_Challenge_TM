class Solution:
    def check_nbr(self, board, m, n, i, j):
        c = 0
        if i-1 >= 0 and board[i-1][j] & 1: # up
            c += 1
        if i-1 >= 0 and j-1 >= 0 and board[i-1][j-1] & 1: # up-left
            c += 1
        if j-1 >= 0 and board[i][j-1] & 1: # left
            c += 1
        if i+1 < m and j-1 >= 0 and board[i+1][j-1] & 1: # down-left
            c += 1
        if i+1 < m and board[i+1][j] & 1: # down
            c += 1
        if i+1 < m and j+1 < n and board[i+1][j+1] & 1: # down-right
            c += 1
        if j+1 < n and board[i][j+1] & 1: # right
            c += 1
        if i-1 >= 0 and j+1 < n and board[i-1][j+1] & 1: # up-right
            c += 1
        return c
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 0 -> 0 = 0
        # 1 -> 0 = 1
        # 0 -> 1 = 2
        # 1 -> 1 = 3
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                x = self.check_nbr(board, m, n, i, j)
                if board[i][j] == 1:
                    if x < 2:
                        board[i][j] = 1
                    elif x == 2 or x == 3:
                        board[i][j] = 3
                    elif x > 3:
                        board[i][j] = 1
                else:
                    if x == 3:
                        board[i][j] = 2
    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2 or board[i][j] == 3:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
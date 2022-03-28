class Solution:
    def dfs(self, board, word, i, j, k, visited):
        # print(i, j)
        visited.add((i, j))
        if k == len(word)-1:
            return 1
        x = 0
        if i-1 >= 0 and board[i-1][j] == word[k+1] and (i-1, j) not in visited: # up
            x += self.dfs(board, word, i-1, j, k+1, visited)
            visited.remove((i-1, j))
        
        if j-1 >= 0 and board[i][j-1] == word[k+1] and (i, j-1) not in visited: # left
            x += self.dfs(board, word, i, j-1, k+1, visited)
            visited.remove((i, j-1))
            
        if i+1 < len(board) and board[i+1][j] == word[k+1] and (i+1, j) not in visited: # down 
            x += self.dfs(board, word, i+1, j, k+1, visited)
            visited.remove((i+1, j))
            
        if j+1 < len(board[0]) and board[i][j+1] == word[k+1] and (i, j+1) not in visited: # right
            x += self.dfs(board, word, i, j+1, k+1, visited)
            visited.remove((i, j+1))
            
        return x
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                k = 0
                visited = set()
                # print(i, j, k)
                if board[i][j] == word[k]:
                    x = self.dfs(board, word, i, j, k, visited)
                    if x:
                        return 1
        return 0
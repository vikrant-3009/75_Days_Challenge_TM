class Solution:
    def dfs(self, grid, n, m, i, j, visited):
        x = 0
        visited[i][j] = 1
        if i-1 >= 0 and grid[i-1][j] == 1 and visited[i-1][j] == 0: # up
            x += 1 + self.dfs(grid, n, m, i-1, j, visited)
        
        if j-1 >= 0 and grid[i][j-1] == 1 and visited[i][j-1] == 0: # left
            x += 1 + self.dfs(grid, n, m, i, j-1, visited)
        
        if i+1 < n and grid[i+1][j] == 1 and visited[i+1][j] == 0: # down
            x += 1 + self.dfs(grid, n, m, i+1, j, visited)
        
        if j+1 < m and grid[i][j+1] == 1 and visited[i][j+1] == 0: # right
            x += 1 + self.dfs(grid, n, m, i, j+1, visited)
            
        return x
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[0]*m for _ in range(n)]
        
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    area = 1 + self.dfs(grid, n, m, i, j, visited)
                    max_area = max(max_area, area)
        
        return max_area
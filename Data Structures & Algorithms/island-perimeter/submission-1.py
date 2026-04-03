class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j):
            print(visited)
            if (min(i, j) < 0 or i >= len(grid) or j >= len(grid[0])
            or not grid[i][j]):
                return 1
            if (i, j) in visited:
                return 0
            
            visited.add((i, j))

            s = sum([dfs(i + 1, j),dfs(i - 1, j),dfs(i, j + 1),dfs(i, j - 1)])
            
            return s

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                   return dfs(i, j)
        
        
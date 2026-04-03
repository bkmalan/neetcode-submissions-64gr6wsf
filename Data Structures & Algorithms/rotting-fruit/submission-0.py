class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        t = 0
        q = []
        fresh = 0
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if col == 1:
                    fresh += 1
                if col == 2:
                    q.append([i,j])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        while q and fresh:
            for i in range(len(q)):
                r,c = q.pop(0)
                for dr,dc in directions:
                    row,col = dr+r,dc+c
                    if not (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1):
                        q.append([row,col])
                        grid[row][col] = 2
                        fresh -= 1
            t += 1
        return -1 if fresh else t 
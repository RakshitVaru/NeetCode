class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        island=0
        ROWS, COLUMNS=len(grid), len(grid[0])
        # amount=0
        
        def dfs(r, c):
            if (min(r,c)<0 or r==ROWS or c==COLUMNS or grid[r][c]==0):
                return
            grid[r][c]=0
            self.amount+=1
            print(self.amount)
            for dr,dc in directions:
                dfs(r+dr, c+dc)

        test=[]
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c]==1:
                    self.amount=0
                    dfs(r,c)
                    test.append(self.amount)
                    island+=1
        return max(test)
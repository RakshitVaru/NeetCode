from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        ROW,COLS=len(grid),len(grid[0])
        queue=deque()
        fresh,time=0,0

        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    queue.append((r,c))

        while queue and fresh>0:
            for i in range(len(queue)):
                r,c = queue.popleft()

                for dr,dc in directions:
                    if (r+dr in range(ROW) and c+dc in range(COLS) and grid[r+dr][c+dc]==1):
                        grid[r+dr][c+dc]=2
                        queue.append((r+dr, c+dc))
                        fresh-=1
            time+=1

        return time if fresh==0 else -1
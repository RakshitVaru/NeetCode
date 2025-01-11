def test(grid):
    m=len(grid)
    n=len(grid[0])
    prev=[0]*n
    
    for i in range(m-1,-1,-1):
    	curr=[0]*n
    	if grid[i][n-1]==1:
    	   curr[n-1]=0
    	else:
    	   curr[n-1]=1
    	for j in range(n-2,-1,-1):
    	    if grid[i][j]==1:
    	        curr[j]=0
    	    else:
    	        curr[j]=curr[j+1]+prev[j]
    	prev=curr
    return prev[0]

print(test([[0,0,0],[0,1,0],[0,0,0]]))
print(test([[0,1],[0,0]]))

print(test([[0,0,0,0],[0,1,1,0],[0,0,0,0]]))
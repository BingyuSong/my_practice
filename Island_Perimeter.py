class Solution(object):
    def islandPerimeter(self, grid):
    	ans=0
    	for i in range(0,len(grid)):
    		for j in range(0,len(grid[i])):
    			if grid[i][j]==1:
    				ans+=4
    				if i>0 and grid[i-1][j]:
    					ans-=2
    				if j>0 and grid[i][j-1]:
    					ans-=2
    	return(ans) 




if __name__=="__main__":
	ans=Solution()
	grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
	print(ans.islandPerimeter(grid))
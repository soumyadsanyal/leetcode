class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        C={}
        m=len(grid)
        n=len(grid[0])
        leftborder=[]
        for row in range(m):
            leftborder.append(grid[row][0])
        for row in range(m+1):
            C[(row,-1)]=sum(leftborder[:row])
        for column in range(n+1):
            C[(-1,column)]=sum(grid[0][:column])
        for row in range(m):
            for column in range(n):
                C[(row,column)]=grid[row][column]+min(C[(row,column-1)],C[(row-1,column)])
        return C[(row,column)]
        
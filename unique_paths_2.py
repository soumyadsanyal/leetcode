class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        C={}
        if obstacleGrid[0][0]==0:
            C[(1,1)]=1
        else:
            C[(1,1)]=0
        for row in range(m+1):
            C[(row,0)]=0
        for column in range(n+1):
            C[(0,column)]=0
        for row in range(1,m+1):
            for column in range(1,n+1):
                if row>1 or column>1:
                    if obstacleGrid[row-1][column-1]==0:
                        C[(row,column)]=C[(row-1,column)]+C[(row,column-1)]
                    else:
                        C[(row,column)]=0
        return C[(m,n)]
        
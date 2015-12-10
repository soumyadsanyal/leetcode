class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        C={}
        C[(1,1)]=1
        for row in range(101):
            C[(row,0)]=0
        for column in range(101):
            C[(0,column)]=0
        for row in range(1,m+1):
            for column in range(1,n+1):
                if row>1 or column>1:
                    C[(row,column)]=C[(row-1,column)]+C[(row,column-1)]
        return C[(m,n)]
        
class Solution(object):
    memo={}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        (self.memo)[0]=1
        (self.memo)[1]=2
        for position in range(2,n):
            (self.memo)[position]=(self.memo)[position-1] + (self.memo)[position-2]
        return self.memo[n-1]
            
            
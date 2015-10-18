class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n==1:
            return x
        if n<0:
            return self.myPow(1/x,-n)
        else:
            if n%2==0:
                return self.myPow(x**2,int(n/2))
            if n%2==1:
                return x*self.myPow(x**2,int(n/2))
                
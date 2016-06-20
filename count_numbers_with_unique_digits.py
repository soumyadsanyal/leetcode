class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 1
        f={}
        f[1]=10
        if n<=1:
            return sum(f.values())
        for k in range(2, n+1):
            temp=9
            for l in range(k-1):
                temp*=(9-l)
            f[k]=temp
        return sum(f.values())

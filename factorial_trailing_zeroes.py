class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        index=1
        count=0
        while 5**index<=n:
            count+=int(n/(5**index))
            index+=1
        return count
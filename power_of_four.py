class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        import math
        return math.log(abs(num), 2)%2==0

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp=num%9
        if temp==0 and num>0:
            return 9
        else:
            return temp
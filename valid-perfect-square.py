class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        temp=1
        if num==1:
            return True
        while temp*temp<=num:
            if temp*temp==num:
                return True
            else:
                temp+=1
        return False

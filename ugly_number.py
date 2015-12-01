class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        while num>1:
            if num%2==0:
                print(num,"\t",2)
                num=num/2
            elif num%3==0:
                print(num,"\t",3)
                num=num/3
            elif num%5==0:
                print(num,"\t",5)
                num=num/5
            else:
                return False
        return True
class Solution(object):
    
    def f(self,y):
        return sum(list(map(lambda x: int(x)**2, list(str(y)))))
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        now=n
        record={}
        while True:
            if now not in record:
                record[now]=1
            next=self.f(now)
            if next==1:
                return True
            if next in record:
                return False
            now=next
class Solution(object):
    import math
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        l=10
        while int(x/l)>0:
            l*=10
        l/=10
        d=math.log(l,10)
        stop=int(d/2)+1
        #print(stop)
        #print(l)
        p=10
        y=x
        z=x
        while stop>0:
            #print(z/l, y%10)
            if int(z/l)!=int(y%10):
                return False
            y=(y-(y%10))/10
            z=(z-int(z/l)*l)
            l/=10
            stop-=1
        return True
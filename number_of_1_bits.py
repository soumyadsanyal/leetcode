class Solution(object):
    
    def findmaxpower(self,dividend,base):
        theindex=0
        while base**(theindex+1)<=dividend:
            theindex+=1
        return theindex
    
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter=0
        while n>0:
            theindex=self.findmaxpower(n,2)
            n=n-2**theindex
            counter+=1
        return counter
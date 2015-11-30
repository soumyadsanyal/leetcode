class Solution(object):
    def __init__(self):
        import string
        self.letters=string.ascii_uppercase
        
    def theint(self,theletter):
        return self.letters.index(theletter)+1
        
    def makelist(self,thestring):
        return list(thestring)
        
    def makeweights(self,thelist):
        return list(zip(thelist,range(len(thelist),0,-1)))
        
    def thevalue(self,pair):
        (letter, position)=pair
        return self.theint(letter)*26**(position-1)
        
    def mapthevalues(self,thestring):
        return list(map(self.thevalue,self.makeweights(self.makelist(thestring))))
    
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(self.mapthevalues(s))
        
        
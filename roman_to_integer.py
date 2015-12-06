class Solution(object):
    def __init__(self):
        temp=list("IVXLCDM")
        self.letters={}
        for index in range(len(temp)):
            self.letters[temp[index]]=index
        self.values={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=[]
        t=list(s)
        before=0
        while t!=[]:
            temp=t.pop()
            after=self.letters[temp]
            if before<=after:
                result.append(self.values[temp])
            else:
                result.append((-1)*self.values[temp])
            before=after
        return sum(result)
            
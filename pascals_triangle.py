class Solution(object):
    
    def prune(self,thelist):
        if thelist==[]:
            return thelist
        temp=[]
        thelist.pop()
        while len(thelist)>1:
            temp.append(thelist.pop())
        return temp
        
        
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal={}
        if numRows<=0:
            return []
        pascal[1]=[0,1,0]
        for row in range(2,numRows+1):
            temp=[0]
            for column in range(1,len(pascal[row-1])):
                temp.append(pascal[row-1][column]+pascal[row-1][column-1])
            temp.append(0)
            pascal[row]=temp
        result=[]
        for row in range(1,numRows+1):
            pascal[row]=self.prune(pascal[row])
            result.append(pascal[row])
        return result
            
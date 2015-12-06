class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascal={}
        pascal[0]=[0,1,0]
        for row in range(1,rowIndex+1):
            temp=[0]
            for column in range(1,len(pascal[row-1])):
                temp.append(pascal[row-1][column]+pascal[row-1][column-1])
            temp.append(0)
            pascal[row]=temp
        a=pascal[rowIndex]
        result=[]
        a.pop()
        while len(a)>1:
            result.append(a.pop())
        return result
        
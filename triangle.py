class Solution(object):
    def themin(self,a,b):
        if a=="X":
            return b
        elif b=="X":
            return a
        else:
            return min(a,b)
    
    def thecombiner(self,first,second):
        result=[]
        for index in range(len(first)):
            if index==0:
                result.append("X")
            else:
                best=self.themin(first[index-1],first[index])
                result.append(best+second[index])
        return result
            
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)
        start=[0,0]
        index=0
        while index<n:
            temp=['X']
            s=[]
            while triangle[index]!=[]:
                s.append(triangle[index].pop())
            while s!=[]:
                temp.append(s.pop())
            result=self.thecombiner(start,temp)
            result.append("X")
            start=result
            index+=1
        values=[term for term in result if term!="X"]
        return min(values)
            
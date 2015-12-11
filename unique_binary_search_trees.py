class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<0:
            return 1
        C={}
        C[0]=1
        C[1]=1
        for i in range(2,n+1):
            temp=[]
            for j in range(i):
                temp.append(C[i-1-j]*C[j])
            C[i]=sum(temp)
        return C[n]
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1==word2:
            return 0
        else:
            D={}
            N=len(word1)
            #print(N)
            M=len(word2)
            #print(M)
            for i in range(N+1):
                D[(i,0)]=i
                #print(i,0,D[(i,0)])
            for j in range(M+1):
                D[(0,j)]=j
                #print(0,j,D[(0,j)])
            for i in range(1,N+1):
                for j in range(1,M+1):
                    #print("looking at %s and %d"%(i,j))
                    left=D[(i-1,j)]+1
                    #print("from left is %d"%left)
                    down=D[(i,j-1)]+1
                    #print("from down is %d"%down)
                    var=0 if word1[i-1]==word2[j-1] else 1
                    #print("var is %d, and the snippets are %s and %s"%(var,word1[:i],word2[:j]))
                    diagonal=D[(i-1,j-1)]+var
                    D[(i,j)]=min(left,down,diagonal)
                    #print(i,j,D[(i,j)])
            return D[(N,M)]
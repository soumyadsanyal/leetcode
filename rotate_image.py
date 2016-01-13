class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N=len(matrix)
        result=[]
        while matrix!=[]:
            result.append(matrix.pop())
        for j in range(N):
            temp=[]
            for i in range(N):
                temp.append(result[i][j])
            matrix.append(temp)
        
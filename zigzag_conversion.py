class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #variables
        pad=numRows-2
        rows=[[] for term in range(numRows)]
        s=list(s)
        s.reverse()
        while s!=[]:
            for jdx in range(len(rows)):
                try:
                    temp=s.pop()
                    rows[jdx].append(temp)
                except:
                    break
            for jdx in range(len(rows)-1, -1, -1):
                try:
                    temp=s.pop()
                    if jdx<=pad and jdx>0:
                        rows[jdx].append(temp)
                    else:
                        s.append(temp)
                except:
                    break
        return ''.join([''.join([term for term in row]) for row in rows]).replace(" ","")

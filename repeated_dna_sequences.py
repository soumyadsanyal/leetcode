class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<10:
            return []
        else:
            h={}
            left=0
            right=10
            result=[]
            while right<len(s)+1:
                candidate=s[left:right]
                if candidate in h and candidate not in result:
                    result.append(candidate)
                else:
                    h[candidate]=1
                left+=1
                right+=1
            return result
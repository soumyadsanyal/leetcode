class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        t=list(s)
        while t!=[]:
            result.append(t.pop())
        return ''.join(result)
        

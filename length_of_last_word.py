class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = []
        trailing=1
        s=list(s)
        while s!=[]:
            temp = s.pop()
            if trailing==1:
                if temp!=' ':
                    result.append(temp)
                    trailing=0
                continue
            if temp!=' ':
                result.append(temp)
            else:
                break
        return len(result)

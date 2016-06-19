class Solution(object):
    import string
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        allowed = string.ascii_lowercase+string.ascii_uppercase+"0123456789"
        result = []
        for idx in range(len(s)):
            temp=s[idx]
            if temp in allowed:
                result.append(temp.lower())
        N=len(result)
        for idx in range(int(len(result)/2)):
            if result[idx]==result[N-1-idx]:
                continue
            else:
                return False
        return True

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #variables
        result=[]
        #routine
        if strs==[]:
            return("")
        for idx in range(min([len(s) for s in strs])):
            test=None
            for s in strs:
                if test is None:
                    test=s[idx]
                else:
                    if s[idx]==test:
                        continue
                    else:
                        return ''.join(result)
            result.append(test)
        return ''.join(result)

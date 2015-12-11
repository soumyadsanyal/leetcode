class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h={}
        for term in strs:
            thekey=str.join("",sorted(term))
            if thekey in h: #and term not in h[thekey]:
                h[thekey].append(term)
            else:
                h[thekey]=[term]
        result=[]
        for k in h.keys():
            temp=h[k]
            temp.sort()
            result.append(temp)
        return result
                
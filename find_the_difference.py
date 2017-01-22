class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hash_s = {}
        hash_t = {}
        # hash s
        rst = s
        while rst!="":
            fst = rst[0]
            rst = rst[1:]
            if fst not in hash_s.keys():
                hash_s[fst]=1
            else:
                hash_s[fst]+=1
        rst = t
        while rst!="":
            fst = rst[0]
            rst = rst[1:]
            if fst not in hash_t.keys():
                hash_t[fst]=1
            else:
                hash_t[fst]+=1
        for k in hash_t.keys():
            if k not in hash_s.keys():
                return k
            lower = hash_s.pop(k)
            higher = hash_t.pop(k)
            if lower < higher:
                return k
                
        

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = pattern
        t = str.split()
        if len(s) != len(t):
            return False
        idx = 0
        h={}
        while idx<len(s):
            source = s[idx]
            target = t[idx]
            if source not in h.keys():
                h[source] = target
            else:
                #source in h, need to check if matches the target according to previous assignment
                if h[source] != target:
                    return False
            idx+=1
        #print(h, h.keys(), h.values())
        return len(set(h.keys())) == len(set(h.values()))
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h={}
        if nums==[]:
            return 0
        while nums!=[]:
            temp=nums.pop()
            lookatkeys=[term for term in h.keys() if term>temp]
            lookatvalues=[h[term] for term in lookatkeys]
            if lookatvalues==[]:
                best=1
            else:
                best=max(lookatvalues)+1
            h[temp]=best
        return max(h.values())
            
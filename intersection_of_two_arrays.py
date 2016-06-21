class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #globals
        h={}
        #routine
        for term in nums1:
            if term in h:
                continue
            if term in nums2:
                h[term]=1
        return h.keys()

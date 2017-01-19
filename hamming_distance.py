class Solution(object):
 
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        unaligned = x ^ y
        count = 0
        while unaligned != 0:
            unaligned = unaligned & (unaligned-1)
            count+=1
        return count
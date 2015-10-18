class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left=0 
        right=x
        mid=left + int((right-left)/2)
        while left<=right:
            if mid*mid<x:
                left=mid+1
                mid=left+int((right-left)/2)
            elif mid*mid>x:
                right=mid-1
                mid=left+int((right-left)/2)
            else:
                return mid
        return right
        
        

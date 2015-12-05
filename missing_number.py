class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=0
        sum=0
        while nums!=[]:
            length+=1
            sum+=nums.pop()
        full=length*(length+1)/2
        return full-sum
        
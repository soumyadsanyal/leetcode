class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=nums[0]
        position=1
        while position<len(nums):
            result=result^nums[position]
            position+=1
        return int(result)
        
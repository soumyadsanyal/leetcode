class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        C={}
        C[-1]=0
        if nums==[]:
            return 0
        C[0]=nums[0]
        for index in range(1,len(nums)):
            C[index]=max(C[index-1],nums[index]+C[index-2])
        result=C.values()
        return max(result)
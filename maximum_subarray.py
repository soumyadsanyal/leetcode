class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return None
        index=1
        best_overall={0:nums[0]}
        best_constrained={0:nums[0]}
        while index<len(nums):
            best_constrained[index]=max(nums[index],nums[index]+best_constrained[index-1])
            best_overall[index]=max(best_overall[index-1],best_constrained[index])
            index+=1
        return best_overall[len(nums)-1]
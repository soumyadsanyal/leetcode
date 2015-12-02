class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        s=1
        index=0
        while index<len(nums):
            result.append(s)
            s=s*nums[index]
            index+=1
        t=1
        index-=1
        while index>=0:
            result[index]=result[index]*t
            t=t*nums[index]
            index=index-1
        return result
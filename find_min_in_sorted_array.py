class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return None
        if len(nums)==1:
            return nums[0]
        else:
            position=1
            while(position<len(nums)):
                if nums[position-1]<=nums[position]:
                    position+=1
                else:
                    break
            if position==len(nums):
                return nums[0]
            else:
                return nums[position]
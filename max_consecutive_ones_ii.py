class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx=0
        count=0
        best=0
        while idx < len(nums):
            if nums[idx]==0:
                if count > best:
                    best = count
                count = 0
            else:
                count+=1
            idx+=1
        if count > best:
            best = count
        return best
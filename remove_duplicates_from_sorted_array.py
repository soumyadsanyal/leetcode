class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h={}
        s=[]
        while nums!=[]:
            temp=nums.pop()
            if temp in h:
                continue
            else:
                h[temp]=1
                s.append(temp)
        while s!=[]:
            nums.append(s.pop())
        return len(nums)
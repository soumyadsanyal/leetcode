class Solution(object):
    def __init__(self):
        self.this=[]
        
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while nums!=[]:
            temp=nums.pop()
            if temp==val:
                continue
            else:
                (self.this).append(temp)
        while self.this!=[]:
            nums.append(self.this.pop())
        return len(nums)
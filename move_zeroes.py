class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pads=[]
        result=[]
        while nums!=[]:
            temp=nums.pop()
            if temp==0:
                pads.append(temp)
            else:
                result.append(temp)
        while result!=[]:
            nums.append(result.pop())
        while pads!=[]:
            nums.append(pads.pop())
        print(nums)
        
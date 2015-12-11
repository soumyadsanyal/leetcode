class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        z=0
        o=0
        t=0
        while nums!=[]:
            temp=nums.pop()
            if temp==0:
                z+=1
            elif temp==1:
                o+=1
            else:
                t+=1
        while z>0:
            nums.append(0)
            z-=1
        while o>0:
            nums.append(1)
            o-=1
        while t>0:
            nums.append(2)
            t-=1
        
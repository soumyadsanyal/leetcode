class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        first=[]
        second=[]
        for index in range(k):
            first.append(nums.pop())
        while nums!=[]:
            second.append(nums.pop())
        while first!=[]:
            nums.append(first.pop())
        while second!=[]:
            nums.append(second.pop())

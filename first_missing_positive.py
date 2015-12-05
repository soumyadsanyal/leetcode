class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h={}
        while nums!=[]:
            temp=nums.pop()
            if temp>=1:
                h[temp]=temp
        index=1
        while True:
            if index not in h:
                return index
            index+=1
        
            
            
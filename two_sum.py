class Solution(object):
    
    def maptempindextonumindex(self,index1,index2, nums, temp):
        first=nums.index(temp[index1])
        second=nums.index(temp[index2])
        if first==second:
            second=nums[first+1:].index(temp[index2]) + first+1
        result=[first+1,second+1]
        result.sort()
        return result
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp=[]
        for term in nums:
            temp.append(term)
        temp.sort()
        for index1 in range(len(temp)):
            for index2 in range(index1+1,len(temp)):
                if temp[index2]>target-temp[index1]:
                    break
                if temp[index2]==target-temp[index1]:
                    return self.maptempindextonumindex(index1,index2, nums, temp)
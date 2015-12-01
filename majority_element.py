class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h={}
        while nums!=[]:
            temp=nums.pop()
            if temp in h:
                h[temp]+=1
            else:
                h[temp]=1
        result=[]
        for (key,value) in h.iteritems():
            result.append((value,key))
        result.sort()
        term=result.pop()
        return term[1]
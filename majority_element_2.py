class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        h={}
        n=len(nums)
        while nums!=[]:
            temp=nums.pop()
            if temp in h:
                h[temp]+=1
            else:
                h[temp]=1
        #print(h)
        threshold=int(n/3)
        result=[]
        for (key,value) in h.iteritems():
            if value>threshold:
                result.append(key)
        return result
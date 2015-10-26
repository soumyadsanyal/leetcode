class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        nums.sort()
        result=[]
        for a in range(len(nums)):
            try:
                if nums[a] + nums[a+1]>0:
                    break
            except:
                break
            for b in range((a+1),len(nums)):
                try:
                    if nums[a] + nums[b] + nums[b+1]>0:
                        break
                except:
                    break
                for c in range(b+1,len(nums)):
                    try:
                        temp = nums[a] + nums[b] + nums[c]
                        if temp>0:
                            break
                        if temp==0:
                            result.append((a,b,c))
                    except:
                        break
        final=[]
        for (first, second, third) in result:
            this=[nums[first],nums[second],nums[third]]
            if this in final:
                continue
            else:
                final.append(this)
        return final
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        """
        position=len(nums)
        h={}
        while True:
            try:
                temp=nums.pop()
                for x in range(temp-t,temp+t+1):
                    if x not in h:
                        continue
                    else:
                        if h[x]-position<=k:
                            return True
                h[temp]=position
                position=position-1
            except:
                return False
                
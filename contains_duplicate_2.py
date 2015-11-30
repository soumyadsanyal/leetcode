class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        thehash={}
        position=len(nums)
        while True:
            try:
                temp=nums.pop()
                if temp in thehash:
                    if abs(thehash[temp]-position)<=k:
                        return True
                else:
                        thehash[temp]=position
                position=position-1
            except:
                return False
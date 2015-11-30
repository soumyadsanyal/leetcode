class Solution(object):
    
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        thehash={}
        while True:
            try:
                temp=nums.pop()
                if temp in thehash:
                    return True
                else:
                    thehash[temp]=1
            except:
                return False
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #make magazine into a hash
        hash = {}
        for idx in range(len(magazine)):
            if magazine[idx] in hash:
                hash[magazine[idx]]+=1
            else:
                hash[magazine[idx]]=1
        #run through ransomNote and see if the note can be constructed
        idx=0
        while idx<len(ransomNote):
            if (ransomNote[idx] not in hash) or (hash[ransomNote[idx]]<=0):
                return False
            else:
                hash[ransomNote[idx]]-=1
            idx+=1
        return True

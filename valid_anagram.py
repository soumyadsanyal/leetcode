class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        first={}
        second={}
        s=list(s)
        t=list(t)
        if len(s)!=len(t):
            return False
        else:
            while s!=[]:
                temp1=s.pop()
                temp2=t.pop()
                if temp1 in first:
                    first[temp1]=first[temp1]+1
                else:
                    first[temp1]=1
                if temp2 in second:
                    second[temp2]=second[temp2]+1
                else:
                    second[temp2]=1
            return first==second
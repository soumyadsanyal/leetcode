class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        best_start=0
        best_end=1
        position=0
        start=0
        end=0
        if s=="":
            return 0
        while position < len(s):
            c=s[position]
            if c in s[start:position]:
                if best_end-best_start<position-start:
                    best_end=position
                    best_start=start
                temp=start
                while s[temp] != c:
                    temp+=1
                start=temp+1
                position+=1
            else:
                position+=1
        return max(best_end-best_start,position-start)
                
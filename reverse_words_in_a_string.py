class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s=="":
            return s
        position=0
        words=[]
        temp=""
        while True:
            while position<len(s) and s[position]!=" ":
                temp+=s[position]
                position+=1
            print(temp)
            if temp!="":
                words.append(temp)
            temp=""
            if position==len(s):
                break
            position+=1
        b=[]
        while words!=[]:
            b.append(words.pop())
        R=str.join(" ",b)
        return R
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        #variables here
        vowels=list("aeiou"+"AEIOU")
        vstore=[]
        intermediate = []
        result=[]
        #routine
        t = list(s)
        for idx in range(len(t)):
            temp=t[idx]
            if temp in vowels:
                vstore.append(temp)
                intermediate.append("\n")
            else:
                intermediate.append(temp)
        for idx in range(len(intermediate)):
            temp=intermediate[idx]
            if temp=="\n":
                result.append(vstore.pop())
            else:
                result.append(temp)
        return ''.join(result)

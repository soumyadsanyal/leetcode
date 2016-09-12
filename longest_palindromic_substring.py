class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = "#" + "#".join(s)+"#"
        P={}    
        i=0
        center=0
        m=0
        while i<len(ss):
            m=2*center-i
            if m in P and center in P and i+P[m]<center+P[center]:
                P[i]=P[m]
            else:
                P[i]=self.search(ss, i)
            if i+P[i]>center+P[center]:
                center=i
            i+=1
        Q={P[k]:k for k in P.keys()}
        bestIndex=Q[max(Q)]
        bestDiameter=P[bestIndex]
        return ss[bestIndex-bestDiameter:bestIndex+bestDiameter+1].replace("#", "")
        
       
    def search(self, s, center):
        i=0
        rEdge=len(s)-1
        while True:
            if center-i-1<0 or center+i+1>rEdge or s[center-i-1]!=s[center+i+1]:
                return i
            else:
                i+=1

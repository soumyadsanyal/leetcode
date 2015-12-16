class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=0
        s=[]
        if digits==[]:
            return []
        place=0
        while digits!=[]:
            temp=digits.pop()
            if place==0:
                temp+=1
                place+=1
            if temp+carry>9:
                carry=1
                temp=0
            else:
                temp+=carry
                carry=0
            s.append(temp)
        if carry==1:
            s.append(carry)
        while s!=[]:
            digits.append(s.pop())
        return digits
        
        
            
                
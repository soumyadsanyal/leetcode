class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num<1:
            return ""
        stack=[]
        while num>0:
            bite=num%10
            stack.append(bite)
            num=(num-bite)//10
        bites=[]
        while stack!=[]:
            bites.append(stack.pop())
        d={}
        d[0]={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
        d[1]={1:"X", 2:"XX", 3:"XXX", 4:"XL", 5:"L", 6:"LX", 7:"LXX", 8:"LXXX", 9:"XC"}
        d[2]={1:"C", 2:"CC", 3:"CCC", 4:"CD", 5:"D", 6:"DC", 7:"DCC", 8:"DCCC", 9:"CM"}
        d[3]={1:"M", 2:"MM", 3:"MMM"}
        place=0
        result=""
        while bites!=[]:
            bite=bites.pop()
            if bite!=0:
                result=d[place][bite]+result
            place+=1
        return result
        
        
class Solution(object):
    
    def match(self,this,that):
        if this=="(" and that==")":
            return True
        elif this=="[" and that=="]":
            return True
        elif this=="{" and that=="}":
            return True
        else:
            return False
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tempstack=[]
        stack=[]
        tempstack=list(s)
        while tempstack!=[]:
            stack.append(str(tempstack.pop()))
        processing=[]
        while stack!=[]:
            newitem=stack.pop()
            if processing!=[]:
                olditem=processing.pop()
                if self.match(olditem,newitem):
                    continue
                else:
                    processing.append(olditem)
                    processing.append(newitem)
            else:
                processing.append(newitem)
        return len(processing)==0
        
        
        
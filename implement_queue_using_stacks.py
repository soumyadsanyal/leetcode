class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1=[]
        self.s2=[]
        
    def f(self,popoption):
        while self.s1!=[]:
            self.s2.append(self.s1.pop())
        temp=self.s2.pop()
        if popoption=="peek":
            result=temp
            self.s2.append(temp)
            temp=result
        while self.s2!=[]:
            self.s1.append(self.s2.pop())
        return temp
            
        
            

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s1.append(x)
        return

    def pop(self):
        """
        :rtype: nothing
        """
        return self.f(popoption="pop")

    def peek(self):
        """
        :rtype: int
        """
        return self.f(popoption="peek")

    def empty(self):
        """
        :rtype: bool
        """
        return self.s1==[]
        
        
        
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.best=None
        self.last=None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x<self.best or self.best is None:
            self.best=x
        self.stack.append(x)
        self.last=x
        

    def pop(self):
        """
        :rtype: void
        """
        if self.stack==[]:
            return
        temp=self.stack.pop()
        if temp<=self.best or self.best is None:
            self.best = min(self.stack) if self.stack!=[] else None
        

    def top(self):
        """
        :rtype: int
        """
        temp=self.stack.pop()
        self.stack.append(temp)
        return temp
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.best
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

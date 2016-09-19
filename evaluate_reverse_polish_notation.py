class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = ["+", "-", "*", "/"]
        values = []
        if tokens==[]:
            return "error"
        for token in tokens:
            if token in operations:
                second = values.pop()
                first = values.pop()
                result = self.do(token, first, second)
                values.append(result)
            else:
                values.append(token)
        return int(values.pop())

    def do(self, op, first, second):
        if op == "+":
            return str(int(first) + int(second))
        if op == "-":
            return str(int(first) - int(second))
        if op == "*":
            return str(int(first) * int(second))
        else:
            if int(first)*int(second)<0:
                return str(-(abs(int(first)) // abs(int(second))))
            else:
                return str(abs(int(first)) // abs(int(second)))

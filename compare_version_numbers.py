class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        first = self.significant([int(x) for x in version1.split(".")])
        second = self.significant([int(x) for x in version2.split(".")])
        if first<second:
            return -1
        if first==second:
            return 0
        else:
            return 1


    def significant(self, l):
        while l!=[]:
            temp = l.pop()
            if temp==0:
                continue
            else:
                l.append(temp)
                break
        return l

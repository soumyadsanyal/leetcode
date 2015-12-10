class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        h={}
        if prices==[]:
            return 0
        else:
            while prices!=[]:
                temp=prices.pop()
                if h.keys()==[]:
                    h[temp]=0
                    highest=temp
                else:
                    if highest>=temp:
                        h[temp]=highest-temp
                    else:
                        h[temp]=0
                        highest=temp
            return max(h.values())
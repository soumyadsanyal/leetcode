class Solution(object):
    
    def P(self,coins,amount):
        if amount in self.Q:
            return Q[amount]
        else:
            return min([1+self.P(coins,amount-coins[index]) for index in range(len(coins)) if coins[index]<=amount])
    
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        Q=[amount+1]*(amount+1)
        Q[0]=0
        for index in range(amount+1):
            for c in coins:
                if index>=c:
                    Q[index]=min(Q[index-c]+1,Q[index])
        if Q[amount]>amount:
            return -1
        else:
            return Q[amount]
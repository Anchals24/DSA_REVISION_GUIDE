"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

"""


from typing import List

class Solution:
    def rec(self, ind, coins, amount, dp):
        if ind == 0:
            if amount % coins[0] == 0:
                return amount // coins[0]
            else:
                return int(1e9)
        if dp[ind][amount] != -1:
            return dp[ind][amount]
        notTake = 0 + self.rec(ind-1, coins, amount, dp)
        take = int(1e9)
        if amount >= coins[ind]:
            take = 1 + self.rec(ind, coins, amount-coins[ind], dp)
        dp[ind][amount] = min(notTake, take)
        return dp[ind][amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = []
        for i in range(n):
            dp.append([-1] * (amount+1))
        result = self.rec(n-1, coins, amount, dp)
        if result  != int(1e9):
            return result
        else:
            return -1
                
        

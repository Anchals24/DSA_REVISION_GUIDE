"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

"""

from typing import List

class Solution:
    def rec(self, ind, coins, amount, dp):
        if ind == 0:
            return 1 if amount % coins[ind] == 0 else 0
        if dp[ind][amount] != -1:
            return dp[ind][amount]
        notTake = self.rec(ind-1, coins, amount, dp)
        take = 0
        if amount >= coins[ind]:
            take = self.rec(ind, coins, amount-coins[ind], dp)
        dp[ind][amount] = notTake + take
        return dp[ind][amount]

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = []
        for i in range(n):
            dp.append([-1] * (amount+1))
        return self.rec(n-1, coins, amount, dp)
        

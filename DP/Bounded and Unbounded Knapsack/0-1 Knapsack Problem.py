"""
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or dont pick it (0-1 property).

Example 1:

Input:
N = 3
W = 4
values[] = {1,2,3}
weight[] = {4,5,1}
Output: 3
Explanation: Choose the last item that weighs 1 unit and holds a value of 3. 

"""

class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def rec(self, ind, wt, val, W, dp):
        
        if ind == 0:
            if W >= wt[ind]:
                return val[ind]
            else:
                return 0
        if dp[ind][W] != -1:
            return dp[ind][W]
        notPick = 0 + self.rec(ind-1, wt, val, W, dp)
        pick = float('-inf')
        if W >= wt[ind]:
            pick = val[ind] + self.rec(ind-1, wt, val, W-wt[ind], dp)
        dp[ind][W] = max(pick, notPick)
        return dp[ind][W]
        
    def knapSack(self,W, wt, val, n):
        dp = [[-1] * (W+1) for _ in range(n)]
        return self.rec(n-1, wt, val, W, dp)

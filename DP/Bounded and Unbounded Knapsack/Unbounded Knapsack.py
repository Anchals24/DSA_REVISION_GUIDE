"""
Given a set of N items, each with a weight and a value, represented by the array w and val respectively. Also, a knapsack with weight limit W.
The task is to fill the knapsack in such a way that we can get the maximum profit. Return the maximum profit.
Note: Each item can be taken any number of times.

Example 1:

Input: 
N = 2
W = 3
val = {1, 1}
wt = {2, 1}
Output: 
3
Explanation: 
1.Pick the 2nd element thrice.
2.Total profit = 1 + 1 + 1 = 3. Also the total weight = 1 + 1 + 1  = 3 which is <= 3.

"""

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        DP = []
        for row in range(N+1):
            column = [-1] * (W+1)
            DP.append(column)
        
        #initialization
        for i in range(N+1):
            for j in range(W+1):
                if i == 0 or j == 0:
                    DP[i][j] = 0
        
        #code
        for i in range(1, N+1):
            for j in range(1, W+1):
                if wt[i-1] <= j:
                    DP[i][j] = max(val[i-1] + DP[i][j-wt[i-1]], DP[i-1][j])
                else:
                    DP[i][j] = DP[i-1][j]
        
        return DP[N][W]
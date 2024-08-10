"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.


Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets. """



class Solution:
    def rec(self, ind, arr, target, dp):
        if target == 0:
            return True
        if ind == 0:
            return arr[ind] == target
        if dp[ind][target] != -1:
            return dp[ind][target]
        pick = False
        if target >= arr[ind]:
            pick = self.rec(ind-1, arr, target-arr[ind], dp)
        notpick = self.rec(ind-1, arr, target, dp)
        
        dp[ind][target] = pick or notpick
        return dp[ind][target]


    def canPartition(self, nums) -> bool:
        arrSum = 0
        for n in nums:
            arrSum += n
        if arrSum % 2 != 0:
            return False
        else:
            n = len(nums)
            target = arrSum//2
            dp = []
            for i in range(n):
                dp.append([-1]* (target+1))
            if self.rec(n-1, nums, target, dp):
                return True
            return False

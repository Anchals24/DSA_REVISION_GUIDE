

"""
Given an integer array nums, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

"""

#Pre-requisite: LIS and Print LIS [Longest Increasing Subsequence]

from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp, cnt = [1] * n , [1] * n
        maxi = -1000000000000
        for ind in range(n):
            for prev in range(0, ind):
                if nums[prev] < nums[ind] and (1 + dp[prev] > dp[ind]):
                    dp[ind] = dp[prev] + 1
                    cnt[ind] = cnt[prev]
                elif nums[prev] < nums[ind] and (1 + dp[prev] == dp[ind]):
                    cnt[ind] += cnt[prev]
            maxi = max(maxi, dp[ind])
        nos = 0
        for i in range(n):
            if dp[i] == maxi:
                nos += cnt[i]
        return nos
        
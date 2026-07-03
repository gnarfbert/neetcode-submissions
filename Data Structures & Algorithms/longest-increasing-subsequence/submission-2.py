class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [1] * (n)
        for i in range(1,n):
            m = 1
            for j in range(0,i):
                if nums[i] > nums[j]:
                    m = max(dp[j] + dp[i], m)
            dp[i] = m
        print(dp)
        
        return max(dp)
        
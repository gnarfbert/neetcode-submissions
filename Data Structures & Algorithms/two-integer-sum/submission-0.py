class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}

        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in dp:
                return sorted([dp[complement], i])
            
            dp[nums[i]] = i
        

        
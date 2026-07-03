class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        currSum = 0
        maxSum = -1001

        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(currSum, maxSum)
        return maxSum
        
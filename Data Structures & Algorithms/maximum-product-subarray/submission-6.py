class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxP = nums[0]
        currMax, currMin = 1,1
        for num in nums:
            tmp = currMax
            currMax = max(num, currMax * num, currMin * num)
            currMin = min(num, tmp * num, currMin * num )
            maxP = max(currMax, maxP)
        
        return maxP
        
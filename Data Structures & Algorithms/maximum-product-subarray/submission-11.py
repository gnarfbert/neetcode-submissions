class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        negP = 1
        posP = 1
        res = nums[0]

        for num in nums:
            tmp = posP * num
            posP = max(posP * num, negP * num, num)
            negP = min(tmp, negP * num, num)
            res = max(posP, res)
        
        return res
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        i = 0
        res = []
        curr = []

        def backtrack(curr, total, i):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            curr.append(nums[i])
            backtrack(curr, total + nums[i], i)
            curr.pop()
            backtrack(curr, total, i+1)

        backtrack(curr, 0, 0)
        
        return res
        
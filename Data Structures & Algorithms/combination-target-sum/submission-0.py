class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        i = 0
        res = []
        curr = []

        def backtrack(curr, i):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or sum(curr) > target:
                return
            curr.append(nums[i])
            backtrack(curr, i)
            curr.pop()
            backtrack(curr, i+1)

        backtrack(curr, 0)
        
        return res
        
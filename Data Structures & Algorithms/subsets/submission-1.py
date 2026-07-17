class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            dfs(i + 1)
            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()
            return
        
        dfs(0)
        return res
        
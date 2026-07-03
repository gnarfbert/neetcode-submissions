class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        minIdx = l

        l, r = 0, minIdx - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] == target:
                return m
            else:
                r = m - 1
        
        l, r = minIdx, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] == target:
                return m
            else:
                r = m - 1
        
        return -1

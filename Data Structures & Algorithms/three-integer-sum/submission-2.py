class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        seen = set()
        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] == 0:
                    curr = (nums[i], nums[j], nums[k])
                    if curr not in seen:
                        seen.add(curr)
                        res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                else:
                    k -= 1
        return res
                    

        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(0, len(heights)-1):
            for j in range(i + 1, len(heights)):
                h = min(heights[i], heights[j])
                dist = j - i
                maxArea = max(maxArea, h * dist)
        
        return maxArea
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        l, r = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l += 1
                r = l + 1
                continue
            r += 1
            maxProf = max(profit, maxProf)


        return maxProf
        
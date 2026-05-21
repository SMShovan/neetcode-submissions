class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mincost = max(prices) + 1;
        for cost in prices:
            if cost > mincost:
                profit = max(0, cost - mincost, profit)
            else:
                mincost = min(mincost, cost)

        return profit
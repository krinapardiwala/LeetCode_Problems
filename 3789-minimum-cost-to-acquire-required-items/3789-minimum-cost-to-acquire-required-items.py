class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        lower = min(need1,need2)
        return lower*min(costBoth,cost1+cost2) + (need1-lower)*min(costBoth,cost1) + (need2-lower)*min(costBoth,cost2)
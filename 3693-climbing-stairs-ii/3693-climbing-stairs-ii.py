class Solution(object):
    def climbStairs(self, n, costs):
        dp_minus_3=dp_minus_2=dp_minus_1=0
        
        for cost in costs:
            current_dp=min(dp_minus_3+9,dp_minus_2+4,dp_minus_1+1)+cost

            dp_minus_3,dp_minus_2,dp_minus_1=(dp_minus_2,dp_minus_1,current_dp)
        
        return dp_minus_1
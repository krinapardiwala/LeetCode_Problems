class Solution(object):
    def minMoves(self, nums):
        moves=0
        n=max(nums)
        for i in nums:
            moves+=(n-i)
        
        return moves
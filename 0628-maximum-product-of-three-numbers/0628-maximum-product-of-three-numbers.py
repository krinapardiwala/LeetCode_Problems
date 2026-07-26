class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()

        max_left=nums[0]*nums[1]*nums[-1]
        max_right=nums[-1]*nums[-2]*nums[-3]

        return max(max_left,max_right)
        
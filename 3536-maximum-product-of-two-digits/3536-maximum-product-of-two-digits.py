class Solution(object):
    def maxProduct(self, n):
        nums=list(str(n))
        nums.sort(reverse=True)
        return (int(nums[0])*int(nums[1]))
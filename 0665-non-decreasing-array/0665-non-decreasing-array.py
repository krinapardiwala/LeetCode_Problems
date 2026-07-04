class Solution(object):
    def checkPossibility(self, nums):
        n=len(nums)
        err=0

        for i in range(1,n):
            if nums[i] < nums[i-1]:
                if err or (i>1 and i<n-1 and nums[i-2]>nums[i] and nums[i+1]<nums[i-1]):
                    return False
                err=1
        return True
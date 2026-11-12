class Solution(object):
    def longestMonotonicSubarray(self, nums):
        max_inc=1
        max_dec=1
        max_len=1
        
        for right in range(len(nums)-1):
            if nums[right+1]<nums[right]:
                max_dec+=1
                max_inc=1
            elif nums[right+1]>nums[right]:
                max_inc+=1
                max_dec=1
            else:
                max_dec=1
                max_inc=1
            
            max_len=max(max_len,max_dec,max_inc)

        return max_len
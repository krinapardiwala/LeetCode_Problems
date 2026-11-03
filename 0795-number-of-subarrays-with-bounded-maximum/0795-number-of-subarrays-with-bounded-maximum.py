class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):

        count=0
        last_invalid=-1
        last_valid=-1

        for i in range(len(nums)):

            if nums[i]>right:
                last_invalid = i

            if nums[i] >= left:
                last_valid = i

            count += max(0, last_valid - last_invalid)

        return count
        
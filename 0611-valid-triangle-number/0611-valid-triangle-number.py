class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        count = 0
        n = len(nums)

        for mid in range(n-1,1,-1): #larger side
            left=0
            right=mid-1

            while left<right:
                if nums[left]+nums[right]>nums[mid]:
                    count+=(right-left) #since array is sorted all elements in the range of right-left will work.
                    right-=1
                else:
                    left+=1
        return count
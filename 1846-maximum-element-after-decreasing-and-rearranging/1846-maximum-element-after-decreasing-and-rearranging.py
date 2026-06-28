class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        arr[0]=1
        left=0
        right=1
        while right<len(arr):
            if abs(arr[right]-arr[left])<=1:
                left+=1
                right+=1
            else:
                arr[right]=1+arr[left]
                left+=1
                right+=1
        return max(arr)
        
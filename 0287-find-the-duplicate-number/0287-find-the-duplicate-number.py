class Solution(object):
    def findDuplicate(self, nums):
        n=[False]*len(nums)
        for i in nums:
            if n[i]:
                return i
            n[i]=True
        return -1


        '''freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for key in freq:
            if freq[key]>1:
                return key
        '''
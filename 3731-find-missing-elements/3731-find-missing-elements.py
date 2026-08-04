class Solution(object):
    def findMissingElements(self, nums):
        freq={}
        for i in nums:
            freq[i]=1

        missing=[]
        for i in range(min(nums),max(nums)+1):
            if i not in freq:
                missing.append(i)
        return missing

'''
def findMissingElements(nums):
    num_set=set(nums)
    missing=[]
    for i in range(min(nums),max(nums)+1):
        if i not in num_set:
            missing.append(i)
    return missing
'''
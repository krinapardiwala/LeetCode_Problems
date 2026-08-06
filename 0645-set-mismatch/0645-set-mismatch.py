class Solution(object):
    def findErrorNums(self, nums):
        duplicate=-1
        seen=set()
        for i in nums:
            if i in seen:
                duplicate=i
            seen.add(i)
        
        for i in range(1,len(nums)+1):
            if i not in seen:
                return [duplicate,i]
class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count=0

        for x in arr1:
            if all(abs(x - y) > d for y in arr2):
                count += 1

        return count
    
    
    
    '''def findTheDistanceValue(self, arr1, arr2, d):
        count=0
        v=0
        left=0
        while left<len(arr1):
            v=0
            for i in arr2:
                if abs(arr1[left]-i)>d:
                    v+=1
            if v==len(arr2):
                count+=1
            left+=1

        return count'''

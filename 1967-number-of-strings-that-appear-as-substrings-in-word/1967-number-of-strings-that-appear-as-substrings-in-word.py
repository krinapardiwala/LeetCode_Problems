class Solution(object):
    def numOfStrings(self, patterns, word):
        count=0
        for substring in patterns:
            if substring in word:
                count+=1
        return count
        
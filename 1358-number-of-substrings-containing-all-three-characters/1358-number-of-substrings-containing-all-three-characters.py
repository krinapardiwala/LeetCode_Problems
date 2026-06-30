class Solution(object):
    def numberOfSubstrings(self, s):
        n=len(s)
        count=0
        freq={'a':0,'b':0,'c':0}
        left=0

        for right in range(n):
            freq[s[right]]+=1
            while freq['a']>0 and freq['b']>0 and freq['c']>0:
                count+=(n-right)
                #this is because once the count of letters is greater than one means the condition is satisfied and all the occurences further would be satisfied. thus we subtract right from the total length of the string so that we obtain the remaining numbe of characters which would be thereby satisfying the condition.
                freq[s[left]]-=1 #we remove the freq. of the leftmost element to slide the window a step towards right.
                left+=1
        return count



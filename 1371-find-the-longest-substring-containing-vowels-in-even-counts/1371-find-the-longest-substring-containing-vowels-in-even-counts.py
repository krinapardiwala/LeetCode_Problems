class Solution(object):
    def findTheLongestSubstring(self, s):
        """
       A bit equal to:
        - 0 means the vowel has appeared an even number of times.
        - 1 means the vowel has appeared an odd number of times.
        """
        mask = 0
        seen = {0: -1}
        max_length = 0

        vowels = {'a': 0,'e': 1,'i': 2,'o': 3,'u': 4}

        for i,j in enumerate(s):
            if j in vowels:
                mask^=(1<<vowels[j]) #Toggle the parity (even/odd state) of this vowel
            if mask in seen:
                max_length=max(max_length,i-seen[mask])
            else:
                seen[mask]=i #tracking mask matters as when the mask repeats, it let's us know the index boundary range where the condition is valid

        return max_length
                
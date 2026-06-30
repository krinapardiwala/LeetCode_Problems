class Solution(object):
    def countVowels(self, word):
        n=len(word)
        count=0
        vowels=set('aeiou')

        for i in range(n):
            if word[i] in vowels:
                count+=((i+1)*(n-i))
        return count
'''the vowel at word[i] can be the start of any substring form i+1 and end of any form n-i.'''
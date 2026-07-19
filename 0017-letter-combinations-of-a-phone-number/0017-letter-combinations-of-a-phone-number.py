class Solution(object):
    def letterCombinations(self, digits):
        map={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        if not digits:
            return []

        def backtrack(index,path):
            if index==len(digits): 
                res.append(''.join(path))
                return
            for i in map[digits[index]]:
                path.append(i)
                backtrack(index+1,path)
                path.pop()
        backtrack(0,[])
        return res

        

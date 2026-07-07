class Solution(object):
    def sumAndMultiply(self, n):
        string=""
        for i in str(n):
            if i != '0':
                string+=i
        if not string:
            return 0
        sum_digits=0
        for i in string:
            sum_digits+=int(i)

        return (int(string)*sum_digits)
        
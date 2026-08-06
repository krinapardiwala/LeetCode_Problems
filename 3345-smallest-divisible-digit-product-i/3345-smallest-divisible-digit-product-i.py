class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            product=1
            for i in str(n):  #typecasting
                product*=int(i)  #getting products
            if product%t==0:  #if product is divisible by t then we return the number itself.
                return n
            n+=1  #or else we increment the number

        
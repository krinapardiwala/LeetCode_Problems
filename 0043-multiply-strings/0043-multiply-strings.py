class Solution(object):
    def multiply(self, num1, num2):
        l1=len(num1)
        l2=len(num2)
        nums={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,}

        def get_number(num,l):
            n=0
            for i,digit in enumerate(num):
                if digit in nums:
                    n=n+(nums[digit]*(10**(l-i-1)))
            return n

        number1=get_number(num1,l1)
        number2=get_number(num2,l2)

        return str(number1*number2)
        
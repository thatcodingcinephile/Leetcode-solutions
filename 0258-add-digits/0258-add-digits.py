class Solution:
    def addDigits(self, num: int) -> int:
             if(num<=9):
                 return num
             else:
                 selfdigit=(num%10+self.addDigits(num//10))
                 return self.addDigits(selfdigit)
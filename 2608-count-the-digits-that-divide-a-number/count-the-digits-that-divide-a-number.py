class Solution:
    def countDigits(self, num: int) -> int:
        if num<=9:
            return 1
        else:
            n=num
            sum1=0
            while n>0:
                c=n%10
                sum1+=1 if num%c==0 else 0
                n//=10
            return sum1